data = list(map(int, input("Masukkan data: ").split()))
cari = int(input("Masukkan data yang dicari: "))

print("Data:", data)

if cari in data:
    print("Data ditemukan di indeks:", data.index(cari))
else:
    print("Data tidak ditemukan")