def bubble_sort_ascending(data):
    n = len(data)
    arr = data.copy()
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Tukar posisi
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f"Iterasi {i + 1}: {arr}")
    
    return arr


# Program utama
data = [15, 8, 22, 3, 10]
print("Data sebelum diurutkan:", data)
print("\nProses Bubble Sort (Ascending):")
hasil = bubble_sort_ascending(data)
print("\nData setelah diurutkan:", hasil)