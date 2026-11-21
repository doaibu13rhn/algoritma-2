try:
    umur = int(input("Masukkan umur Anda: "))
    if umur < 0:
        print("Umur tidak boleh negatif.")
    else:
        print(f"Umur Anda adalah {umur} tahun.")
except ValueError:
    print("Kesalahan: Input tidak valid! Harap masukkan angka saja, bukan huruf.")