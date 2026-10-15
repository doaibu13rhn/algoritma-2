mahasiswa = ["Andi", "Budi", "Citra", "Dina", "Eko"]

nama = input("Masukkan nama mahasiswa yang ingin dicari: ")

posisi = -1
for i in range(len(mahasiswa)):
    if mahasiswa[i] == nama:
        posisi = i
        break

if posisi != -1:
    print(f"Nama {nama} ditemukan pada indeks ke-{posisi} (diurutan ke-{posisi + 1}).")
else:
    print(f"Nama {nama} tidak ditemukan dalam daftar.")