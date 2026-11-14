def shell_sort_descending(data):
    n = len(data)
    arr = data.copy()
    
    gap = n // 2
    
    while gap > 0:
        print(f"\n--- Gap = {gap} ---")
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Ubah > menjadi < untuk descending
            while j >= gap and arr[j - gap] < temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            print(f"  Setelah proses i={i}: {arr}")
        gap //= 2
    
    return arr


# Program utama
data = [25, 17, 31, 13, 2]
print("Data sebelum diurutkan:", data)
print("\nProses Shell Sort (Descending):")
hasil = shell_sort_descending(data)
print("\nData setelah diurutkan:", hasil)