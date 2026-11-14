def bubble_sort_descending(data):
    n = len(data)
    arr = data.copy()
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # Ubah tanda > menjadi < untuk descending
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Iterasi {i + 1}: {arr}")
    
    return arr


# Program utama
data = [15, 8, 22, 3, 10]
print("Data sebelum diurutkan:", data)
print("\nProses Bubble Sort (Descending):")
hasil = bubble_sort_descending(data)
print("\nData setelah diurutkan:", hasil)