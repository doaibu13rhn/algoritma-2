def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    langkah = 0
    
    while low <= high:
        langkah += 1
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid, langkah
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, langkah

print("--- Latihan 3: Pencarian String ---")
list_nama = ["Andi", "Budi", "Citra", "Dewi", "Eka", "Fajar"]
target_nama = "Dewi"

indeks_nama, langkah_nama = binary_search(list_nama, target_nama)

if indeks_nama != -1:
    print(f"Nama '{target_nama}' ditemukan pada indeks {indeks_nama}.")
else:
    print(f"Nama '{target_nama}' tidak ditemukan.")
print(f"Jumlah langkah pencarian: {langkah_nama} langkah.")