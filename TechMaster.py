from abc import ABC, abstractmethod

# 1. ABSTRACTION: Menggunakan Abstract Class
class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar, stok):
        # 2. ENCAPSULATION: Menggunakan Private Attribute (__)
        self.nama = nama
        self.__harga_dasar = harga_dasar
        self.__stok = 0
        self.set_stok(stok) # Validasi awal saat pembuatan

    # Getter untuk Stok
    def get_stok(self):
        return self.__stok

    # Getter untuk Harga Dasar
    def get_harga_dasar(self):
        return self.__harga_dasar

    # Setter dengan Validasi (Encapsulation)
    def set_stok(self, jumlah):
        if jumlah >= 0:
            self.__stok = jumlah
            return True
        else:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

# 3. INHERITANCE: Kelas Laptop mewarisi BarangElektronik
class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok, processor):
        super().__init__(nama, harga_dasar, stok)
        self.processor = processor

    # 4. POLYMORPHISM: Override Method
    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.10
        return (self.get_harga_dasar() + pajak) * jumlah

    def tampilkan_detail(self, jumlah):
        pajak_per_unit = self.get_harga_dasar() * 0.10
        subtotal = self.hitung_harga_total(jumlah)
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")
        print(f"   Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(10%): Rp {pajak_per_unit:,.0f}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")
        return subtotal

# 3. INHERITANCE: Kelas Smartphone mewarisi BarangElektronik
class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok, kamera):
        super().__init__(nama, harga_dasar, stok)
        self.kamera = kamera

    # 4. POLYMORPHISM: Override Method
    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga_dasar() * 0.05
        return (self.get_harga_dasar() + pajak) * jumlah

    def tampilkan_detail(self, jumlah):
        pajak_per_unit = self.get_harga_dasar() * 0.05
        subtotal = self.hitung_harga_total(jumlah)
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")
        print(f"   Harga Dasar: Rp {self.get_harga_dasar():,.0f} | Pajak(5%): Rp {pajak_per_unit:,.0f}")
        print(f"   Beli: {jumlah} unit | Subtotal: Rp {subtotal:,.0f}")
        return subtotal

# 4. POLYMORPHISM: Fungsi Independen untuk Proses Transaksi
def proses_transaksi(keranjang):
    print("\n--- STRUK TRANSAKSI ---")
    total_tagihan = 0
    for i, item in enumerate(keranjang, 1):
        barang = item['objek']
        jumlah = item['jumlah']
        print(f"{i}. ", end="")
        subtotal = barang.tampilkan_detail(jumlah)
        total_tagihan += subtotal
    
    print("-" * 40)
    print(f"TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
    print("-" * 40)

# --- ALUR PROGRAM (User Story) ---

# 1. Admin membuat data produk
print("--- SETUP DATA ---")
laptop1 = Laptop("ROG Zephyrus", 20000000, 10, "Ryzen 9")
print(f"Berhasil menambahkan stok {laptop1.nama}: {laptop1.get_stok()} unit.")

hp1 = Smartphone("iPhone 13", 15000000, 0, "12MP")
# 2. Admin mencoba mengisi stok negatif
hp1.set_stok(-5) 
# Update stok yang benar
if hp1.set_stok(20):
    print(f"Berhasil menambahkan stok {hp1.nama}: {hp1.get_stok()} unit.")

# 3. User membeli barang
keranjang_belanja = [
    {"objek": laptop1, "jumlah": 2},
    {"objek": hp1, "jumlah": 1}
]

# 4. Menampilkan struk
proses_transaksi(keranjang_belanja)