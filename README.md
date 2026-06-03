# 🎓 EduGuard: Student Dropout Early Warning System

## 📖 Deskripsi Proyek

**EduGuard** merupakan sistem peringatan dini (*Early Warning System*) berbasis Machine Learning yang dirancang untuk membantu institusi pendidikan tinggi dalam mengidentifikasi mahasiswa yang berpotensi mengalami putus kuliah (*dropout*).

Melalui analisis data akademik dan administratif mahasiswa, sistem ini mampu memberikan prediksi risiko dropout secara cepat dan akurat sehingga pihak kampus dapat melakukan intervensi lebih awal untuk meningkatkan tingkat keberhasilan studi mahasiswa.

Proyek ini dikembangkan sebagai bagian dari **Final Project Machine Learning** pada program **Google Developer Groups on Campus (GDGoC) Telkom University 2026**.

---

# 🌍 Penyelarasan Sustainable Development Goals (SDGs)

## SDG 4: Pendidikan Berkualitas (Quality Education)

<p align="justify">
Pendidikan merupakan salah satu faktor utama dalam pembangunan sumber daya manusia yang berkualitas. Namun, tingginya angka mahasiswa yang tidak menyelesaikan pendidikan menjadi tantangan bagi berbagai institusi pendidikan tinggi.

Melalui EduGuard, kami berupaya mendukung pencapaian <strong>Sustainable Development Goal (SDG) 4: Quality Education</strong> dengan memanfaatkan teknologi Machine Learning untuk mendeteksi risiko putus kuliah sejak dini. Dengan adanya sistem ini, institusi pendidikan dapat mengambil langkah preventif dan memberikan dukungan yang lebih tepat sasaran kepada mahasiswa yang membutuhkan.
</p>

---

# 🎯 Tujuan Proyek

Proyek ini bertujuan untuk:

- Mengidentifikasi mahasiswa yang berisiko mengalami putus kuliah.
- Membantu dosen wali dan pihak akademik dalam proses monitoring mahasiswa.
- Menyediakan sistem pendukung keputusan berbasis data.
- Meningkatkan tingkat retensi mahasiswa.
- Mendukung implementasi SDG 4: Pendidikan Berkualitas.

---

# 🚀 Fitur Utama

### 📊 Prediksi Risiko Dropout

Memprediksi kemungkinan mahasiswa akan:

- Lulus (Graduate)
- Putus Kuliah (Dropout)

### ⚡ Analisis Real-Time

Prediksi dilakukan secara langsung melalui dashboard interaktif menggunakan Streamlit.

### 📈 Visualisasi Probabilitas

Menampilkan probabilitas hasil prediksi dalam bentuk grafik sehingga lebih mudah dipahami.

### 📝 Rekomendasi Intervensi

Memberikan rekomendasi tindakan berdasarkan hasil prediksi yang diperoleh.

### 🎓 Fokus pada Pendidikan

Dirancang khusus untuk mendukung kebutuhan institusi pendidikan tinggi dalam melakukan monitoring akademik mahasiswa.

---

# 🧠 Metodologi Machine Learning

## 1. Pengumpulan Data

Dataset yang digunakan berisi informasi mahasiswa yang mencakup:

- Data demografi
- Data akademik
- Status administrasi
- Performa semester awal

---

## 2. Data Preprocessing

Tahapan yang dilakukan meliputi:

- Pembersihan data (*data cleaning*)
- Penanganan data kosong (*missing values*)
- Transformasi data
- Standarisasi fitur numerik

---

## 3. Feature Engineering

Beberapa fitur tambahan dibuat untuk meningkatkan performa model:

### Total_Approved_Units

Jumlah total mata kuliah yang berhasil diselesaikan mahasiswa.

```text
Total_Approved_Units =
Approved Semester 1 + Approved Semester 2
```

### Grade_Incentive

Perubahan performa akademik antara semester 1 dan semester 2.

```text
Grade_Incentive =
Grade Semester 2 - Grade Semester 1
```

---

## 4. Pelatihan Model

Model Machine Learning dilatih menggunakan dataset yang telah diproses dan kemudian diekspor menjadi:

```text
model_dropout.pkl
```

Selain itu digunakan juga:

```text
scaler_dropout.pkl
selected_features.pkl
```

untuk memastikan konsistensi proses prediksi pada aplikasi deployment.

---

# 📥 Parameter Input

EduGuard menerima beberapa parameter utama sebagai masukan:

| Parameter | Keterangan |
|------------|------------|
| Mata Kuliah Lulus Semester 1 | Jumlah mata kuliah yang berhasil diselesaikan |
| IP Semester 1 | Indeks Prestasi Semester pertama |
| Mata Kuliah Lulus Semester 2 | Jumlah mata kuliah yang berhasil diselesaikan |
| IP Semester 2 | Indeks Prestasi Semester kedua |
| Status Pembayaran UKT | Status administrasi mahasiswa |
| Usia Saat Mendaftar | Usia mahasiswa ketika masuk perguruan tinggi |

---

# 📤 Hasil Prediksi

Sistem akan menghasilkan:

### Status Mahasiswa

- Aman (Berpotensi Lulus)
- Berisiko Tinggi (Berpotensi Dropout)

### Probabilitas Prediksi

Contoh:

```text
Probabilitas Lulus     : 87.45%
Probabilitas Dropout  : 12.55%
```

### Rekomendasi Akademik

Sistem akan memberikan saran tindak lanjut berdasarkan hasil prediksi.

---

# 🖥️ Struktur Proyek

```text
EduGuard/
│
├── EduGuard.ipynb
├── app.py
├── data.csv
├── model_dropout.pkl
├── scaler_dropout.pkl
├── selected_features.pkl
├── README.md
└── requirements.txt
```

Keterangan:

| File | Fungsi |
|--------|---------|
| EduGuard.ipynb | Notebook untuk eksplorasi data, preprocessing, dan pelatihan model |
| app.py | Aplikasi Streamlit untuk deployment |
| data.csv | Dataset yang digunakan |
| model_dropout.pkl | Model Machine Learning yang telah dilatih |
| scaler_dropout.pkl | Objek standarisasi fitur |
| selected_features.pkl | Daftar fitur yang digunakan model |

---

# 🛠️ Teknologi yang Digunakan

### Bahasa Pemrograman

- Python

### Library Data Science

- Pandas
- NumPy
- Scikit-Learn

### Visualisasi Data

- Matplotlib
- Seaborn

### Deployment

- Streamlit

### Model Serialization

- Joblib

---

# ▶️ Cara Menjalankan Proyek

## 1. Clone Repository

```bash
git clone https://github.com/username/EduGuard.git
cd EduGuard
```

## 2. Install Dependency

```bash
pip install -r requirements.txt
```

## 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

## 4. Buka Browser

```text
http://localhost:8501
```

---

# 👨‍💻 Profil Kelompok

## Nama Kelompok

**Tim Deny Pengen Pulang Kampung**

### Anggota Tim

- Guidomelvin
- Deny Pratama Sukardi
- Berto Jdoyvan Purba
- Almer Fakhir Arwonio

---

# 🎓 Program

Proyek ini dikembangkan dalam rangka memenuhi Tugas Besar Machine Learning pada program:

**Google Developer Groups on Campus (GDGoC) Telkom University Bandung 2026**

---

# 💡 Kontribusi Proyek

EduGuard diharapkan dapat menjadi solusi awal bagi institusi pendidikan untuk:

- Mengurangi angka putus kuliah.
- Meningkatkan keberhasilan studi mahasiswa.
- Mendukung pengambilan keputusan berbasis data.
- Mewujudkan pendidikan yang lebih inklusif dan berkualitas.

---

# 📜 Lisensi

Proyek ini dibuat untuk tujuan pendidikan, pembelajaran, dan pengembangan akademik dalam lingkup Tugas Besar Machine Learning GDGoC Universitas Telkom.
