class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_data(self):
        print("Nama :", self.nama)
        print("NIM  :", self.nim)

class MahasiswaTI(Mahasiswa):
    def belajar_pemrograman(self):
        print(f"{self.nama} sedang belajar pemrograman")


mhs = MahasiswaTI("Muhamad Raihan", "251011400314")

mhs.tampilkan_data()
mhs.belajar_pemrograman()