# 🎓 Panduan Presentasi: Stunting Agent (MLOps Project)

Dokumen ini adalah panduan untuk presentasi Tugas Akhir MLOps. Fokus presentasi adalah pada **masalah yang diselesaikan**, **arsitektur teknis (MLOps)**, dan **demonstrasi solusi**.

---

## ⏱️ Struktur Presentasi (Estimasi 10-15 Menit)

1.  **Pembukaan & Latar Belakang** (2 Menit)
2.  **Solusi & Fitur** (2 Menit)
3.  **Arsitektur Teknis (The "MLOps" Part)** (4 Menit) - *Bagian Paling Penting!*
4.  **Live Demo** (3 Menit)
5.  **Kesimpulan & Tanya Jawab** (2 Menit)

---

## 1. Pembukaan & Latar Belakang
*   **Slide 1: Judul & Tim**
    *   "Halo, kami dari kelompok [Nama Kelompok]. Hari ini kami akan mempresentasikan **Stunting Agent: Edukator Gizi Berbasis AI**."
    *   Perkenalkan anggota tim dan peran masing-masing.

*   **Slide 2: Masalah (The "Why")**
    *   **Konteks**: "Stunting masih menjadi isu kritis di Indonesia. Prevalensi 2024 ada di **19.8%**, padahal target pemerintah **14%**."
    *   **Pain Point**: "Informasi gizi seringkali sulit diakses, membosankan, atau terlalu teknis bagi masyarakat umum."
    *   **Relevansi SDGs**: "Proyek ini mendukung **SDG 2 (Zero Hunger)** dan **SDG 3 (Good Health)**."

---

## 2. Solusi: Stunting Agent
*   **Slide 3: Apa itu Stunting Agent?**
    *   "Kami membangun Chatbot AI yang bisa diajak ngobrol layaknya konsultan gizi pribadi."
    *   **Value Proposition**:
        *   **Personal**: Menjawab pertanyaan spesifik user.
        *   **Akurat**: Berbasis data (bukan halusinasi) menggunakan RAG.
        *   **Terjangkau**: Memberikan rekomendasi menu murah meriah (berdasarkan data harga pangan BPS).

---

## 3. Arsitektur Teknis (Deep Dive MLOps)
*Ini adalah bagian inti untuk mata kuliah MLOps. Jelaskan bagaimana sistem bekerja di belakang layar.*

*   **Slide 4: High-Level Architecture**
    *   Gambarkan alur: `User -> Web UI -> Flask API -> Agent -> RAG -> Gemini -> Response`.

*   **Slide 5: RAG (Retrieval-Augmented Generation)**
    *   Jelaskan kenapa pakai RAG: "Agar AI tidak 'sok tahu' (halusinasi). Kita menyuplai 'otak' tambahan berupa data valid."
    *   **Data Source**: `stunting_2024.txt` (Kemenkes) & `food_prices_2024.txt` (BPS).
    *   **Vector DB**: Menggunakan **ChromaDB** untuk pencarian cepat.
    *   **Embeddings**: Menggunakan **Local Embeddings (`sentence-transformers`)**.
        *   *Point Plus*: "Kami menggunakan local embeddings untuk menghemat biaya API dan mengurangi latensi network."

*   **Slide 6: Tech Stack & Deployment**
    *   **LLM**: Google Gemini (Cerdas & Cepat).
    *   **Backend**: Flask (Python).
    *   **Containerization**: **Docker**.
        *   *Point Plus*: "Aplikasi kami sudah containerized, siap dideploy di mana saja (Cloud/On-Premise) tanpa masalah dependensi ('it works on my machine')."

---

## 4. Skenario Live Demo
*Jangan cuma klik-klik asal. Gunakan skenario cerita (Storytelling).*

1.  **Buka Aplikasi**: Tunjukkan halaman awal yang modern.
2.  **Skenario Chat**:
    *   *User*: "Saya ibu muda, anak saya susah makan sayur. Ada ide menu murah gak? Budget saya terbatas."
    *   *Action*: Ketik pertanyaan tersebut.
    *   *Highlight*: Tunjukkan bagaimana bot menjawab dengan **resep spesifik** dan **estimasi harga** (karena dia punya data harga pasar).
    *   *Highlight*: Tunjukkan fitur **Read Receipts (Ceklis Dua)** dan **Typing Indicator**.
3.  **Navigasi Info**:
    *   Klik tab **Info**. Tunjukkan grafik tren stunting (Chart.js). Jelaskan bahwa ini data real.
4.  **Navigasi Berita**:
    *   Klik tab **Berita**. Tunjukkan integrasi berita dengan gambar HD. Klik salah satu untuk bukti link valid.
5.  **Error Handling (Opsional tapi Keren)**:
    *   Jika berani, matikan koneksi internet sebentar lalu kirim chat. Tunjukkan pesan error yang ramah ("Maaf, sedang ada gangguan..."). Ini menunjukkan *system robustness*.

---

## 5. Penutup
*   **Slide 7: Kesimpulan**
    *   "Stunting Agent bukan sekadar chatbot, tapi langkah kecil teknologi untuk membantu menyehatkan bangsa."
    *   "Secara teknis, kami berhasil mengimplementasikan pipeline RAG yang efisien dan deployment yang scalable menggunakan Docker."

*   **Slide 8: Q&A**
    *   "Terima kasih. Kami siap menjawab pertanyaan."

---

## 💡 Tips Tambahan untuk MLOps
*   Jika ditanya **"Kenapa pakai ChromaDB lokal?"**, jawab: "Untuk skala proyek ini, ChromaDB lokal paling efisien, mudah disetup, dan tidak butuh server terpisah."
*   Jika ditanya **"Bagaimana kalau datanya berubah?"**, jawab: "Sistem RAG kami dinamis. Kami tinggal update file `.txt` di folder data, dan sistem akan meng-index ulang saat restart. Untuk production, bisa dibuat pipeline otomatis (CI/CD) untuk update data."
