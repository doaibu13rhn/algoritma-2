class Rekening:
    def __init__(self, nama_pemilik, nomor_rekening, saldo):
        self.nama_pemilik = nama_pemilik
        self.nomor_rekening = nomor_rekening
        self.saldo = saldo
    
    def tampilkan_saldo(self):
        print(f"Saldo saat ini: Rp{self.saldo:,}".replace(",", "."))
    
    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"Setor: Rp{jumlah:,}".replace(",", "."))
    
    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi!")
        else:
            self.saldo -= jumlah
            print(f"Tarik: Rp{jumlah:,}".replace(",", "."))


rekening = Rekening("Budi Santoso", "1234567890", 1000000)

print("=== Saldo Awal ===")
rekening.tampilkan_saldo()

print("\n=== Setor Dana ===")
rekening.setor(500000)

print("\n=== Saldo Setelah Setor ===")
rekening.tampilkan_saldo()

print("\n=== Tarik Dana ===")
rekening.tarik(250000)

print("\n=== Saldo Akhir ===")
rekening.tampilkan_saldo()