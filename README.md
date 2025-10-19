# 💰 Aplikasi Keuangan Sederhana

Aplikasi web sederhana untuk mencatat **pemasukan dan pengeluaran keuangan pribadi**.  
Dibuat menggunakan **Python (Flask)** dan **HTML/CSS (Bootstrap)** agar mudah digunakan dan ringan dijalankan secara lokal.

---

## 🚀 Fitur Utama

- ✏️ **Catat Transaksi**
  - Input tanggal, kategori, jenis transaksi (pemasukan/pengeluaran), jumlah, dan catatan.
- 📊 **Laporan Keuangan**
  - Menampilkan total pemasukan, pengeluaran, dan saldo.
  - Menampilkan daftar transaksi yang sudah dicatat.
- 💾 **Penyimpanan Lokal**
  - Menggunakan SQLite (default Flask) untuk menyimpan data secara lokal.

---

## 🛠️ Teknologi yang Digunakan

- **Backend:** Python + Flask  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Database:** SQLite  
- **Template Engine:** Jinja2  

---
## 📂 Struktur Proyek

```

Aplikasi-Keuangan-Sederhana/
│
├── instance/               # Folder database SQLite
├── templates/              # File HTML untuk tampilan (catat transaksi & laporan)
├── venv/                   # Virtual environment (opsional)
├── app.py                  # File utama Flask
└── README.md               # Dokumentasi proyek

````

---

## ⚙️ Cara Menjalankan Aplikasi

### 1️⃣ Clone Repository
```bash
git clone https://github.com/zxkky/Aplikasi-Keuangan-Sederhana.git
cd Aplikasi-Keuangan-Sederhana
````

### 2️⃣ Aktifkan Virtual Environment (opsional)

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / MacOS:**

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install flask
```

### 4️⃣ Jalankan Aplikasi

```bash
python app.py
```

### 5️⃣ Buka di Browser

```
http://127.0.0.1:5000
```

## 👨‍💻 Pengembang

**Nama:** zxkky
**Proyek:** Aplikasi Keuangan Sederhana
**Versi:** 1.0.0
**Lisensi:** MIT License


> 📘 *Proyek ini dibuat untuk latihan dan pembelajaran dasar Flask serta manajemen keuangan pribadi.*

