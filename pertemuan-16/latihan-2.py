buah = ["Apel", "Jeruk", "Mangga", "Pisang", "Anggur"]
print("Daftar buah:", buah)

try:
    indeks = int(input(f"Masukkan indeks buah (0 sampai {len(buah) - 1}): "))
    print(f"Buah pada indeks ke-{indeks} adalah: {buah[indeks]}")
except IndexError:
    print(f"Kesalahan: Indeks di luar jangkauan! Masukkan angka antara 0 hingga {len(buah) - 1}.")
except ValueError:
    print("Kesalahan: Indeks harus berupa bilangan bulat.")