def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

# Mengisi array secara manual
arr = [64, 34, 25, 12, 22, 11, 90]

print("Array asal:")
for i in range(len(arr)):
    print("%d" %arr[i])

bubbleSort(arr)

print("\nArray setelah diurutkan menggunakan Bubble Sort:")
for i in range(len(arr)):
    print("%d" %arr[i])

insertionSort(arr)

print("\nArray setelah diurutkan menggunakan Insertion Sort:")
for i in range(len(arr)):
   print("%d" %arr[i])
