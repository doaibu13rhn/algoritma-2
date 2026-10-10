nama = ["Andi", "Budi", "Citra", "Dina", "Eka", "Fajar", "Gita"]

def linear_search(data, target):
    for j in range(len(data)):
        if data[j] == target:
            return j
    return -1

cari = input("Masukkan nama yang dicari: ")
hasil = linear_search(nama, cari)

if hasil != -1:
    print("Data ditemukan di indeks:", hasil)
else:
    print("Data tidak ditemukan")