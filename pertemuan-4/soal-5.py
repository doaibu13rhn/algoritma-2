class Produk:
    def __init__(self, nama_produk, harga, jumlah):
        self.nama_produk = nama_produk
        self.harga = harga
        self.jumlah = jumlah
    
    def tampilkan_produk(self):
        print(f"Nama Produk    : {self.nama_produk}")
        print(f"Harga Satuan   : Rp{self.harga:,}".replace(",", "."))
        print(f"Jumlah Beli    : {self.jumlah}")
    
    def hitung_total(self):
        return self.harga * self.jumlah
    
    def diskon(self, persen):
        total = self.hitung_total()
        nilai_diskon = total * persen / 100
        total_setelah_diskon = total - nilai_diskon
        return nilai_diskon, total_setelah_diskon


print("=" * 40)
print("PRODUK 1")
print("=" * 40)
produk1 = Produk("Laptop Asus", 8000000, 2)

produk1.tampilkan_produk()

total1 = produk1.hitung_total()
print(f"Total Sebelum Diskon : Rp{total1:,}".replace(",", "."))


diskon1, total_akhir1 = produk1.diskon(10)
print(f"Besarnya Diskon (10%) : Rp{diskon1:,.0f}".replace(",", "."))
print(f"Total Setelah Diskon  : Rp{total_akhir1:,.0f}".replace(",", "."))


print("\n" + "=" * 40)
print("PRODUK 2")
print("=" * 40)
produk2 = Produk("Samsung Galaxy", 5000000, 3)

produk2.tampilkan_produk()

total2 = produk2.hitung_total()
print(f"Total Sebelum Diskon : Rp{total2:,}".replace(",", "."))


diskon2, total_akhir2 = produk2.diskon(15)
print(f"Besarnya Diskon (15%) : Rp{diskon2:,.0f}".replace(",", "."))
print(f"Total Setelah Diskon  : Rp{total_akhir2:,.0f}".replace(",", "."))