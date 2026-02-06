# 📊 Analisis dan Visualisasi Data Nilai Siswa

## 🧮 Hasil Analisis

1. **Mapel mana yang memiliki rata-rata nilai tertinggi?**  
   ➤ Mata pelajaran **Matematika** memiliki rata-rata nilai tertinggi.  
   Hal ini terlihat dari data yang menunjukkan sebagian besar siswa memperoleh nilai di atas rata-rata pada mapel ini.

2. **Mapel mana yang memiliki nilai terendah?**  
   ➤ Mata pelajaran **Bahasa Inggris** memiliki nilai terendah.  
   Terdapat beberapa siswa dengan nilai rendah, sehingga menurunkan rata-rata keseluruhan mapel ini.

3. **Bagaimana visualisasi membantu dalam memahami data?**  
   ➤ Visualisasi membantu kita **melihat pola dan perbandingan antar mapel dengan cepat**.  
   Dengan grafik batang atau diagram, kita bisa langsung mengetahui mata pelajaran yang unggul dan yang perlu ditingkatkan tanpa harus membaca tabel data secara detail.

---

## 🧠 Refleksi Siswa

1. **Apa hal baru yang kamu pelajari dari kegiatan analisis dan visualisasi data?**  
   ➤ Saya belajar cara **mengolah data menjadi informasi yang berguna**, seperti menghitung rata-rata, median, dan modus.  
   Saya juga memahami bagaimana **grafik membantu menyampaikan informasi data secara visual dan menarik**.

2. **Kesulitan apa yang kamu alami dalam membuat grafik?**  
   ➤ Kesulitan saya adalah **menentukan jenis grafik yang tepat** dan **mengatur tampilannya agar mudah dibaca**.  
   Kadang hasil grafik tidak sesuai harapan karena kesalahan dalam pemilihan kolom data atau format angka.

3. **Menurut kamu, apakah AI membantu dalam analisis sebuah data?**  
   ➤ Ya, **AI sangat membantu** dalam analisis data karena bisa **mengolah data secara cepat, akurat, dan otomatis**.  
   Dengan AI, kita bisa membuat visualisasi, menghitung statistik, bahkan menemukan pola yang sulit dilihat secara manual.

---

## 🗂️ Kesimpulan
Kegiatan ini membantu saya memahami bahwa **data tidak hanya angka**, tetapi juga informasi yang bisa dianalisis untuk mengambil keputusan.  
Visualisasi dan AI membuat proses analisis data menjadi lebih mudah, menarik, dan efisien.


# 📑 Laporan Praktikum OOP & Proyek "TechMaster"

Repositori ini berisi dokumentasi lengkap pengerjaan tugas praktikum 1-6 serta penyelesaian Proyek Integrasi Sistem Manajemen Inventaris Elektronik menggunakan bahasa pemrograman Python.

---

## 📋 Analisis Praktikum (Latihan 1-6)

### 1. Implementasi Pilar OOP
* **Abstraction**: Menggunakan abstract class `GameUnit` dan `BarangElektronik` sebagai kontrak dasar agar setiap objek memiliki standar metode yang sama.
* **Encapsulation**: Melindungi data sensitif seperti `__hp`, `__stok`, dan `__harga_dasar` menggunakan *Private Attribute* agar tidak bisa dimodifikasi secara ilegal dari luar class.
* **Inheritance**: Class anak (seperti `Mage`, `Laptop`, atau `Smartphone`) mewarisi sifat dasar dari parent class untuk meningkatkan efisiensi dan pengorganisasian kode.
* **Polymorphism**: Memungkinkan objek yang berbeda untuk merespons perintah yang sama (seperti `.serang()` atau `.hitung_harga_total()`) dengan cara yang berbeda-beda sesuai karakteristiknya.

### 2. Jawaban Tugas Analisis 6 (Polymorphism)
* **Uji Skalabilitas (Class Healer)**:
  * **Pertanyaan**: Apakah program berjalan lancar setelah menambah class `Healer`?
  * **Jawaban**: **Ya, berjalan lancar.** Objek `Healer` dapat langsung masuk ke dalam list `pasukan` tanpa mengubah kode perulangan `for` sedikit pun.
  * **Kesimpulan**: Keuntungan Polimorfisme adalah kemudahan dalam mengupdate konten (seperti karakter baru) secara cepat tanpa merusak struktur kode inti yang sudah stabil.
* **Konsistensi Penamaan**:
  * **Pertanyaan**: Apa yang terjadi jika nama metode diubah menjadi `tembak_panah`?
  * **Jawaban**: Program akan mengalami **Error (AttributeError)** karena fungsi pemanggil tidak menemukan metode `.serang()` pada objek tersebut.
  * **Kesimpulan**: Nama metode harus persis sama karena Polimorfisme bekerja berdasarkan "kontrak" antarmuka yang seragam agar satu perintah bisa dijalankan oleh berbagai jenis objek.

---

## 🖥️ Logika & Output Program

### A. Output Pertarungan (Latihan 1-6)
```text
--- Pertarungan Dimulai ---
Layla menyerang Zilong!
Zilong terkena damage 15. Sisa HP: 105
Zilong menyerang Layla!
Layla terkena damage 20. Sisa HP: 80

--- Update Class Hero (Mage) ---
Eudora [Mage] | HP: 80 | Mana: 100
Eudora menyerang Balmond!
Balmond terkena damage 30. Sisa HP: 170
Eudora menggunakan Fireball ke Balmond!
Balmond terkena damage 60. Sisa HP: 110

--- PERANG DIMULAI (Polymorphism) ---
Eudora (Mage)   : menembakkan Bola Api! Boom!
Miya (Archer)   : memanah dari jauh! Jleb!
Zilong (Fighter): memukul dengan pedang! Slash!
Gord (Mage)     : menembakkan Bola Api! Boom!

### Output Proyek Integrasi (TechMaster)

--- SETUP DATA ---
✅ Berhasil menambahkan stok ROG Zephyrus: 10 unit.
❌ Gagal update stok iPhone 13! Stok tidak boleh negatif (-5).
✅ Berhasil menambahkan stok iPhone 13: 20 unit.

--- STRUK TRANSAKSI ---
1. [LAPTOP] ROG Zephyrus | Proc: Ryzen 9
   Harga Dasar: Rp 20,000,000 | Pajak (10%): Rp 2,000,000
   Beli: 2 unit | Subtotal: Rp 44,000,000

2. [SMARTPHONE] iPhone 13 | Cam: 12MP
   Harga Dasar: Rp 15,000,000 | Pajak (5%): Rp 750,000
   Beli: 1 unit | Subtotal: Rp 15,750,000

-------------------------------------------------------
TOTAL TAGIHAN: Rp 59,750,000
-------------------------------------------------------