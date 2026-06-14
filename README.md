# 🥗 Stunting Agent - Edukator Gizi

Video Demo: http://bit.ly/3LI7fxl

## 📝 Abstraksi

Stunting masih menjadi masalah kesehatan masyarakat yang mendesak di Indonesia. Meskipun prevalensi stunting telah turun menjadi 19.8% pada tahun 2024, angka ini masih perlu ditekan untuk mencapai target pemerintah sebesar 14%. Stunting tidak hanya berdampak pada pertumbuhan fisik, tetapi juga perkembangan kognitif anak, yang pada akhirnya mempengaruhi kualitas Sumber Daya Manusia (SDM) Indonesia di masa depan.

Proyek Stunting Agent ini dikembangkan sebagai solusi berbasis Artificial Intelligence (AI) untuk memberikan edukasi yang mudah diakses mengenai pencegahan stunting dan rekomendasi gizi yang terjangkau.

### 🌍 Kontribusi pada SDGs
Proyek ini mendukung **Sustainable Development Goals (SDGs)** PBB:
*   **SDG 2: Zero Hunger (Tanpa Kelaparan)** - Meningkatkan nutrisi dan mengakhiri segala bentuk malnutrisi.
*   **SDG 3: Good Health and Well-being (Kehidupan Sehat dan Sejahtera)** - Menjamin kehidupan yang sehat dan meningkatkan kesejahteraan bagi semua usia.

### 🎓 Konteks Akademis
Aplikasi ini dibuat untuk memenuhi Tugas Akhir Mata Kuliah **Machine Learning Operations (MLOps)** pada Semester 3 di Binus University. Proyek ini mendemonstrasikan penerapan siklus hidup ML (Machine Learning Lifecycle), mulai dari manajemen data, pengembangan model RAG (Retrieval-Augmented Generation), hingga deployment aplikasi berbasis container.

---

## 🚀 Fitur Utama

*   **🤖 AI Chatbot Cerdas**: Menggunakan **Google Gemini** yang diperkuat dengan **RAG (Retrieval-Augmented Generation)** untuk memberikan jawaban yang akurat berdasarkan data Kemenkes dan BPS.
*   **📚 Edukasi Interaktif**: Menyediakan informasi tentang urgensi stunting dan grafik tren penurunan stunting di Indonesia.
*   **📰 Berita Terkini**: Menyajikan update berita terbaru seputar penanganan stunting dari sumber terpercaya.
*   **💬 User-Friendly Interface**: Antarmuka modern dengan fitur *read receipts* (ceklis dua), indikator mengetik, dan navigasi yang responsif.
*   **🔒 Session Management**: Mendukung percakapan multi-user secara bersamaan tanpa tercampur.

---

## 📂 Struktur Folder

```
Salinan AOL_MLPOPS/
├── data/                       # Sumber data untuk RAG
│   ├── stunting_2024.txt       # Data statistik stunting Kemenkes
│   └── food_prices_2024.txt    # Data harga pangan BPS
├── stunting_agent/             # Core logic agen AI
│   ├── agent.py                # Definisi agen dan tools
│   └── rag.py                  # Engine RAG (ChromaDB + Embeddings)
├── templates/                  # Frontend
│   └── index.html              # Single Page Application (UI)
├── app.py                      # Server Flask (Backend API)
├── Dockerfile                  # Konfigurasi Container
├── requirement.txt             # Daftar dependensi Python
└── README.md                   # Dokumentasi Proyek
```

---

## 🛠️ Instalasi & Penggunaan

### Prasyarat
*   Python 3.10+
*   Google Gemini API Key

### 1. Clone Repository
```bash
git clone <repository-url>
```

### 2. Setup Environment
Buat file `.env` di dalam folder `stunting_agent/` dan isi dengan API Key Anda:
```env
GOOGLE_API_KEY=your_api_key_here
```

Install dependensi:
```bash
pip install -r requirement.txt
```

### 3. Jalankan Aplikasi (Lokal)
```bash
python app.py
```
Buka browser dan akses: `http://localhost:8080`

### 4. Jalankan dengan Docker
```bash
# Build image
docker build -t stunting-agent .

# Run container
docker run -p 8080:8080 -e GOOGLE_API_KEY=your_api_key_here stunting-agent
```

---

## 👥 Tim Pengembang

Proyek ini dikerjakan oleh kelompok mahasiswa Binus University:

1.  **Akmal Dwi Putra Mahardika** (NIM: 2802505374)
2.  **Ivan Yudhistira** (NIM: 2802555580)
3.  **Muhammad Reza Al-Ghifari** (NIM: 2802555044)
4.  **Rifa Naftali Azka** (NIM: 2802495726)

---

## 🔧 Tech Stack

*   **Backend**: Flask, Gunicorn
*   **AI/ML**: Google Gemini, SentenceTransformers (Local Embeddings), ChromaDB (Vector Store)
*   **Frontend**: HTML5, CSS3, JavaScript, Chart.js
*   **Deployment**: Docker, Railway (Support)

---
*Dibuat dengan ❤️ untuk Indonesia yang lebih sehat.*
