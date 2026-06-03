# ==============================================================================
# TUGAS BESAR MACHINE LEARNING - Tim Deny Pengen Pulang Kampung
# EduGuard: Sistem Peringatan Dini Risiko Putus Kuliah Mahasiswa
# ==============================================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Konfigurasi Halaman Aplikasi
st.set_page_config(
    page_title="EduGuard: Dashboard Pemantauan SDG 4", 
    layout="centered"
)

# 2. Pemuatan Model dan Artefak Komputasi
try:
    model = joblib.load('model_dropout.pkl')
    scaler = joblib.load('scaler_dropout.pkl')
    selected_features = joblib.load('selected_features.pkl')
except FileNotFoundError:
    st.error("Berkas model ('model_dropout.pkl') atau scaler ('scaler_dropout.pkl') tidak ditemukan.")
    st.info("Silakan pastikan seluruh tahapan pada Jupyter Notebook telah dijalankan hingga selesai untuk mengekspor berkas model.")
    st.stop()

# 3. Judul dan Deskripsi Konteks Proyek
st.title("EduGuard: Sistem Peringatan Dini Risiko Putus Kuliah Mahasiswa")
st.markdown("""
Aplikasi ini dikembangkan untuk mendukung implementasi pilar **SDG 4 (Pendidikan Berkualitas)**. 
Sistem ini berfungsi sebagai instrumen prediksi untuk mendeteksi risiko mahasiswa putus kuliah (*dropout*) 
secara dini berdasarkan indikator aktivitas akademis dan profil administrasi mereka.
""")
st.write("---")

# 4. Informasi Panel Samping (Sidebar)
st.sidebar.header("Pusat Kontrol Akademik")
st.sidebar.markdown("""
**Panduan Penggunaan:**
1. Masukkan data capaian akademis mahasiswa pada formulir yang tersedia.
2. Klik tombol **Analisis Risiko Mahasiswa**.
3. Sistem akan menghitung probabilitas status keberlanjutan studi secara real-time.
""")
st.sidebar.write("---")
st.sidebar.caption("Tim Deny Pengen Pulang Kampung © 2026 - GDGoC Telkom University Bandung")

# 5. Formulir Input Parameter Evaluasi Mahasiswa
st.subheader("Formulir Evaluasi Kinerja Mahasiswa")
st.write("Silakan masukkan parameter akademis mahasiswa di bawah ini:")

# Pembagian tata letak input menjadi dua kolom utama
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Capaian Akademis Semester 1**")
    approved_1st = st.number_input("Jumlah Mata Kuliah Lulus Semester 1", min_value=0, max_value=30, value=5, step=1)
    
    # Input menggunakan skala IPK Indonesia (0.00 - 4.00)
    ipk_1st = st.slider("Indeks Prestasi Semester 1 (Skala 4.0)", min_value=0.00, max_value=4.00, value=3.00, step=0.01)
    # Proses konversi otomatis ke skala 20 di balik layar
    grade_1st = (ipk_1st / 4.00) * 20.0
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Status Administrasi**")
    tuition = st.selectbox(
        "Status Pembayaran Uang Kuliah", 
        options=[1, 0], 
        format_func=lambda x: "Tepat Waktu / Lunas" if x == 1 else "Terdapat Tunggakan"
    )

with col2:
    st.markdown("**Capaian Akademis Semester 2**")
    approved_2nd = st.number_input("Jumlah Mata Kuliah Lulus Semester 2", min_value=0, max_value=30, value=5, step=1)
    
    # Input menggunakan skala IPK Indonesia (0.00 - 4.00)
    ipk_2nd = st.slider("Indeks Prestasi Semester 2 (Skala 4.0)", min_value=0.00, max_value=4.00, value=3.00, step=0.01)
    # Proses konversi otomatis ke skala 20 di balik layar
    grade_2nd = (ipk_2nd / 4.00) * 20.0
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Profil Demografi**")
    age = st.number_input("Usia Saat Mendaftar Kuliah", min_value=15, max_value=60, value=19, step=1)

st.write("<br>", unsafe_allow_html=True)

# 6. Pemrosesan Data dan Integrasi Rekayasa Fitur
if st.button("Analisis Risiko Mahasiswa", type="primary"):
    
    # Definisi seluruh struktur kolom sesuai dataset latih asal
    all_columns = [
        'Marital status', 'Application mode', 'Application order', 'Course',
        'Daytime/evening attendance', 'Previous qualification', 'Previous qualification (grade)',
        'Nacionality', 'Mother\'s qualification', 'Father\'s qualification', 'Mother\'s occupation',
        'Father\'s occupation', 'Admission grade', 'Displaced', 'Educational special needs', 'Debtor',
        'Tuition fees up to date', 'Gender', 'Scholarship holder', 'Age at enrollment', 'International',
        'Curricular units 1st sem (credited)', 'Curricular units 1st sem (enrolled)', 'Curricular units 1st sem (evaluations)',
        'Curricular units 1st sem (approved)', 'Curricular units 1st sem (grade)', 'Curricular units 1st sem (without evaluations)',
        'Curricular units 2nd sem (credited)', 'Curricular units 2nd sem (enrolled)', 'Curricular units 2nd sem (evaluations)',
        'Curricular units 2nd sem (approved)', 'Curricular units 2nd sem (grade)', 'Curricular units 2nd sem (without evaluations)',
        'Unemployment rate', 'Inflation rate', 'GDP', 'Total_Approved_Units', 'Grade_Incentive'
    ]
    
    # Inisialisasi DataFrame satu baris dengan nilai default 0.0
    input_df = pd.DataFrame(0.0, index=[0], columns=all_columns)
    
    # Pemetaan variabel input pengguna ke kolom DataFrame
    input_df['Curricular units 1st sem (approved)'] = approved_1st
    input_df['Curricular units 1st sem (grade)'] = grade_1st
    input_df['Tuition fees up to date'] = tuition
    input_df['Curricular units 2nd sem (approved)'] = approved_2nd
    input_df['Curricular units 2nd sem (grade)'] = grade_2nd
    input_df['Age at enrollment'] = age
    
    # Rekayasa Fitur (Feature Engineering) sesuai dengan spesifikasi model
    input_df['Total_Approved_Units'] = approved_1st + approved_2nd
    input_df['Grade_Incentive'] = grade_2nd - grade_1st
    
    # Standarisasi data pada fitur numerik kontinu
    numerical_features = ['Age at enrollment', 'Admission grade', 'Previous qualification (grade)', 
                          'Total_Approved_Units', 'Grade_Incentive', 'Curricular units 1st sem (grade)', 
                          'Curricular units 2nd sem (grade)']
    input_df[numerical_features] = scaler.transform(input_df[numerical_features])
    
    # Pelaksanaan Inferensi/Prediksi dengan Model Random Forest
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]
    
    # 7. Output Hasil Analisis
    st.write("---")
    st.subheader("Hasil Analisis Sistem:")
    
    if prediction == 1:
        prob_dropout = probability[1] * 100
        st.error(f"**STATUS: BERISIKO TINGGI (POTENSI PUTUS KULIAH / DROPOUT)** — Probabilitas: {prob_dropout:.2f}%")
        
        st.markdown("""
        **Rekomendasi Intervensi Akademis:**
        * Mahasiswa yang bersangkutan terindikasi membutuhkan perhatian atau bimbingan khusus dari dosen wali sesegera mungkin.
        * Penurunan metrik kelulusan mata kuliah atau indeks nilai semester berjalan menjadi indikator utama kerentanan akademis.
        * Disarankan untuk menjadwalkan evaluasi personal atau program pendampingan intensif.
        """)
    else:
        prob_graduate = probability[0] * 100
        st.success(f"**STATUS: AMAN (POTENSI LULUS / GRADUATE)** — Probabilitas Bertahan: {prob_graduate:.2f}%")
        
        st.markdown("""
        **Rekomendasi Tindakan:**
        * Mahasiswa menunjukkan konsistensi dan performa belajar yang memenuhi standar kelulusan reguler.
        * Disarankan untuk mempertahankan pola belajar yang ada serta didorong untuk berpartisipasi dalam program pengembangan kompetensi tambahan.
        """)
        
    # Visualisasi komparatif hasil prediksi dalam bentuk grafik batang
    st.write("<br>", unsafe_allow_html=True)
    st.markdown("**Grafik Distribusi Probabilitas Hasil Analisis:**")
    chart_data = pd.DataFrame({
        'Status Kelulusan': ['Lulus (Graduate)', 'Putus Kuliah (Dropout)'],
        'Probabilitas (%)': [probability[0]*100, probability[1]*100]
    })
    
    fig, ax = plt.subplots(figsize=(6, 2))
    colors = ['#2ecc71', '#e74c3c'] 
    sns.barplot(x='Probabilitas (%)', y='Status Kelulusan', data=chart_data, palette=colors, ax=ax)
    ax.set_xlim(0, 100)
    ax.set_xlabel('Persentase Probabilitas (%)')
    ax.set_ylabel('')
    st.pyplot(fig)