def shell_sort_nama(data):
    n = len(data)
    arr = data.copy()
    
    gap = n // 2
    
    while gap > 0:
        print(f"\n--- Gap = {gap} ---")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Bandingkan string case-insensitive
            while j >= gap and arr[j - gap].lower() > temp.lower():
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print(f"  Setelah proses i={i}: {arr}")
        gap //= 2
    
    return arr


# Program utama
mahasiswa = ["Rina", "Andi", "Budi", "Sinta", "Dewi", "Citra"]
print("Daftar mahasiswa sebelum diurutkan:")
print(mahasiswa)

print("\nProses Shell Sort (Alfabet):")
hasil = shell_sort_nama(mahasiswa)

print("\nDaftar mahasiswa setelah diurutkan (A-Z):")
for i, nama in enumerate(hasil, start=1):
    print(f"{i}. {nama}")