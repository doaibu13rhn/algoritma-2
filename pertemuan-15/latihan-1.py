def shell_sort_ascending(data):
    n = len(data)
    arr = data.copy()
    
    # Tentukan gap awal (biasanya n // 2), lalu bagi 2 setiap iterasi
    gap = n // 2
    
    while gap > 0:
        print(f"\n--- Gap = {gap} ---")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Bandingkan elemen yang berjarak 'gap'
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print(f"  Setelah proses i={i}: {arr}")
        gap //= 2
    
    return arr


# Program utama
data = [25, 17, 31, 13, 2]
print("Data sebelum diurutkan:", data)
print("\nProses Shell Sort (Ascending):")
hasil = shell_sort_ascending(data)
print("\nData setelah diurutkan:", hasil)