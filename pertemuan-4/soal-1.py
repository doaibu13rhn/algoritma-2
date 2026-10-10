class Mahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def tampilkan_data(self):
        print("=" * 30)
        print(f"Nama  : {self.nama}")
        print(f"NIM   : {self.nim}")
        print(f"Prodi : {self.prodi}")
        print("=" * 30)


# Membuat 2 objek mahasiswa
mahasiswa1 = Mahasiswa("Fathi", "251011400302", "Teknik Informatika")
mahasiswa2 = Mahasiswa("Caca", "251011400217", " Teknik informatika")

# Menampilkan data kedua mahasiswa
mahasiswa1.tampilkan_data()
mahasiswa2.tampilkan_data()