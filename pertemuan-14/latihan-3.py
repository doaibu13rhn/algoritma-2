def bubble_sort_nama(data):
    n = len(data)
    arr = data.copy()
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Bandingkan string (case-insensitive agar lebih rapi)
            if arr[j].lower() > arr[j + 1].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Iterasi {i + 1}: {arr}")
    
    return arr


# Program utama
mahasiswa = ["Kayla", "Raihan", "Nurul", "Dina", "Abi", "Rifqi"]
print("Daftar mahasiswa sebelum diurutkan:")
print(mahasiswa)

print("\nProses Bubble Sort (Alfabet):")
hasil = bubble_sort_nama(mahasiswa)

print("\nDaftar mahasiswa setelah diurutkan (A-Z):")
for i, nama in enumerate(hasil, start=1):
    print(f"{i}. {nama}")