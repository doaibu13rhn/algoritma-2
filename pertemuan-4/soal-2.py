class Laptop:
    def __init__(self, merk, warna, ram, harga):
        self.merk = merk
        self.warna = warna
        self.ram = ram
        self.harga = harga

    def tampilkan_info(self):
        print("=== Informasi Laptop ===")
        print(f"Merk  : {self.merk}")
        print(f"Warna : {self.warna}")
        print(f"RAM   : {self.ram} GB")
        print(f"Harga : Rp{self.harga:,}")
        print()

    def nyalakan(self):
        print(f"Laptop {self.merk} sedang dinyalakan...")
        print()


laptop1 = Laptop("Lenovo", "Hitam", 8, 5000000)
laptop2 = Laptop("ASUS", "Silver", 16, 8000000)

laptop1.tampilkan_info()
laptop1.nyalakan()

laptop2.tampilkan_info()
laptop2.nyalakan()