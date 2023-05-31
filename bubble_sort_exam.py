#Andika Pratama
#10109007

def bubble_sort(arr):
    n = len(arr)
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 

nilai_siswa = [78, 65, 90, 82, 70] 
bubble_sort(nilai_siswa) 
print("Daftar nilai yang diurutkan:") 
for nilai in nilai_siswa:
    print(nilai)