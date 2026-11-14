def merge_sort(arr, descending=False):
    
    if len(arr) <= 1:
        return arr

    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    
    left_sorted = merge_sort(left_half, descending)
    right_sorted = merge_sort(right_half, descending)

    return merge(left_sorted, right_sorted, descending)


def merge(left, right, descending):
    result = []
    i = j = 0

    
    while i < len(left) and j < len(right):
        if not descending: 
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else: 
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result



# LATIHAN 1

print("=== Latihan 1: Mengurutkan Data (Ascending) ===")
data_angka = [45, 12, 78, 34, 23, 89]
print(f"Data sebelum: {data_angka}")
hasil_ascending = merge_sort(data_angka)
print(f"Data sesudah: {hasil_ascending}\n")



# LATIHAN 2

print("=== Latihan 2: Mengurutkan Data (Descending) ===")
print(f"Data sebelum: {data_angka}")

hasil_descending = merge_sort(data_angka, descending=True)
print(f"Data sesudah: {hasil_descending}\n")



# LATIHAN 3

print("=== Latihan 3: Mengurutkan Nama Mahasiswa ===")
data_mahasiswa = ["Zaki", "Budi", "Andi", "Citra", "Dewi", "Fajar"]
print(f"Data sebelum: {data_mahasiswa}")

hasil_alfabet = merge_sort(data_mahasiswa)
print(f"Data sesudah: {hasil_alfabet}")