#Muhamad Maulana Yusuf S
#10109034

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

angka_andi = [9, 5, 3, 8, 2]
selection_sort(angka_andi)
print("Daftar angka yang diurutkan:")
for angka in angka_andi:
    print(angka)