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


📑 Laporan Praktikum OOP & Proyek Integrasi "TechMaster"Repositori ini mendokumentasikan perjalanan pembelajaran Pemrograman Berorientasi Objek (OOP) melalui 6 modul latihan dan satu proyek tantangan integrasi.🚀 Analisis Praktikum (Latihan 1 - 6)⚔️ Logika Pertarungan & InteraksiPada tahap awal, kita berhasil mengimplementasikan interaksi antar objek. Penggunaan super() pada class Mage memungkinkan pewarisan atribut dari class Hero sambil menambahkan fitur unik seperti Mana.Output Program:Plaintext--- Pertarungan Dimulai ---
Layla menyerang Zilong!
Zilong terkena damage 15. Sisa HP: 105
Zilong menyerang Layla!
Layla terkena damage 20. Sisa HP: 80

--- Update Class Hero (Mage) ---
Eudora [Mage] | HP: 80 | Mana: 100
Eudora menggunakan Fireball ke Balmond!
Balmond terkena damage 60. Sisa HP: 110
🛡️ Keamanan Data (Encapsulation)Implementasi Private Attribute (__hp) menjamin integritas data. HP tidak bisa dimanipulasi secara ilegal dari luar class. Jika input tidak valid (negatif atau terlalu besar), Setter akan melakukan koreksi otomatis.🎭 Analisis Mendalam: Polimorfisme (Latihan 6)Berikut adalah jawaban atas pertanyaan analisis pada Modul 6:1. Uji Skalabilitas (Penambahan Class Healer)Pertanyaan: Apakah program berjalan lancar?Jawaban: Ya, program berjalan sangat lancar. Meskipun kita menambahkan objek dari class baru (Healer) ke dalam list pasukan, kode perulangan for pahlawan in pasukan: tetap bisa mengeksekusi method .serang() tanpa perlu dimodifikasi sedikit pun.Kesimpulan: Keuntungan Polimorfisme bagi programmer adalah fleksibilitas dan skalabilitas. Kita bisa menambah konten baru (karakter, item, atau fitur) ke dalam game tanpa harus membongkar kode lama yang sudah stabil. Kode menjadi lebih bersih dan mudah dikembangkan.2. Konsistensi Penamaan (Method Archer)Pertanyaan: Apa yang terjadi jika method serang diubah menjadi tembak_panah?Jawaban: Program akan mengalami Error (AttributeError). Saat perulangan memanggil pahlawan.serang(), Python tidak menemukan method tersebut pada objek Archer karena namanya telah berubah.Alasan Konsistensi Penamaan: Dalam Polimorfisme, nama method bertindak sebagai "Kontrak". Agar berbagai objek berbeda dapat diperlakukan dengan cara yang sama dalam satu perintah (interfase tunggal), nama method-nya harus persis sama. Jika berbeda, fungsi pemanggil tidak akan mengenali perintah tersebut.🛠️ Proyek Integrasi: "TechMaster"Proyek ini menggabungkan keempat pilar OOP ke dalam sistem manajemen stok toko elektronik.1. Implementasi Pilar OOPPilarImplementasi dalam ProyekAbstractionMenggunakan BarangElektronik sebagai kelas abstrak agar tidak bisa dibuat objek barang "umum".EncapsulationMenyembunyikan stok dan harga dasar menggunakan __.InheritanceLaptop dan Smartphone mewarisi properti dasar dari parent class.PolymorphismMethod hitung_harga_total memberikan hasil berbeda sesuai jenis pajak barang.2. Hasil Eksekusi Program (Struk Transaksi)Plaintext--- SETUP DATA ---
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