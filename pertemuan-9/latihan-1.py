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

# ==========================================
# LATIHAN 1 & 2: Mencari Angka & Menampilkan Langkah
# ==========================================
print("--- Latihan 1 & 2: Pencarian Angka ---")
list_angka = [5, 10, 15, 20, 25, 30]
target_angka = 25

indeks, jumlah_langkah = binary_search(list_angka, target_angka)

if indeks != -1:
    print(f"Angka {target_angka} ditemukan pada indeks {indeks}.")
else:
    print(f"Angka {target_angka} tidak ditemukan.")
print(f"Jumlah langkah pencarian: {jumlah_langkah} langkah.\n")