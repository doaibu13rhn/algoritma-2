def merge_sort(arr, descending=False):
    # Base case: jika array memiliki 0 atau 1 elemen, maka sudah terurut
    if len(arr) <= 1:
        return arr

    # Membagi array menjadi dua bagian
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Memanggil rekursif untuk mengurutkan masing-masing bagian
    left_sorted = merge_sort(left_half, descending)
    right_sorted = merge_sort(right_half, descending)

    # Menggabungkan kembali bagian yang sudah terurut
    return merge(left_sorted, right_sorted, descending)


def merge(left, right, descending):
    result = []
    i = j = 0

    # Membandingkan elemen dari kedua array
    while i < len(left) and j < len(right):
        if not descending: # Ascending (A-Z atau kecil ke besar)
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else: # Descending (Z-A atau besar ke kecil)
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    # Memasukkan sisa elemen (jika ada)
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


# ==========================================
# LATIHAN 1
# ==========================================
print("=== Latihan 1: Mengurutkan Data (Ascending) ===")
data_angka = [45, 12, 78, 34, 23, 89]
print(f"Data sebelum: {data_angka}")
hasil_ascending = merge_sort(data_angka)
print(f"Data sesudah: {hasil_ascending}\n")


# ==========================================
# LATIHAN 2
# ==========================================
print("=== Latihan 2: Mengurutkan Data (Descending) ===")
print(f"Data sebelum: {data_angka}")
# Memanggil fungsi dengan parameter descending=True
hasil_descending = merge_sort(data_angka, descending=True)
print(f"Data sesudah: {hasil_descending}\n")


# ==========================================
# LATIHAN 3
# ==========================================
print("=== Latihan 3: Mengurutkan Nama Mahasiswa ===")
data_mahasiswa = ["Zaki", "Budi", "Andi", "Citra", "Dewi", "Fajar"]
print(f"Data sebelum: {data_mahasiswa}")
# Python secara otomatis membandingkan string berdasarkan urutan alfabet (ASCII)
hasil_alfabet = merge_sort(data_mahasiswa)
print(f"Data sesudah: {hasil_alfabet}")