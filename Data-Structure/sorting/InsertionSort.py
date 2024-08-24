def InsertionSort(array):
    b = 1
    array_length = len(array)
    if array_length <= 1:
        return array
    while b <= array_length-1:
        if array[b-1] > array[b]:
            array[b], array[b-1] = array[b-1], array[b]
            if b-1 > 0:
                b -= 1
            else: b += 1
        elif array[b-1] <= array[b]:
            b += 1
    
    return array









my_array = [64, 34, 25, 12, 22, 11, 90, 5]

print(InsertionSort(my_array))