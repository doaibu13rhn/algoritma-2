data = [75, 80, 65, 90, 85, 70, 95]

cari = int(input("Input nilai yang inginf dicari: "))

posisi = -1
for i in range(len(data)):
    if data[i] == cari:
        posisi = i
        break

if posisi != -1:
    print(f"Nilai {cari} ditemukan pada indeks ke-{posisi} (diurutan-{posisi + 1}).")
else:
    print(f"Nilai {cari} tidak ditemukan dalam dagtar.")