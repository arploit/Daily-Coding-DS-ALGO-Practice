def recursionSort(arr, count):
    j = 0
    if count <= 0:
        return

    while j < len(arr) - 1:
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

        j += 1

    recursionSort(arr, count - 1)


newArray = [4, 1, 0]

recursionSort(newArray, len(newArray) - 1)
print(newArray)
