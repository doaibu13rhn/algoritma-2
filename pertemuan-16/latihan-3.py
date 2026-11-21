nama_file = input("Masukkan nama file teks (contoh: data.txt): ")

try:
    with open(nama_file, "r", encoding="utf-8") as file:
        isi = file.read()
        print("\n--- Isi File ---")
        print(isi)
except FileNotFoundError:
    print(f"Pesan Khusus: Maaf, file '{nama_file}' tidak ditemukan. Pastikan nama dan lokasi file sudah benar.")
except Exception as e:
    print(f"Terjadi kesalahan lain saat membaca file: {e}")