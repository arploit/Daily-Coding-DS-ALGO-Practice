def sortingAlgo(array_to_sorted):
    starting_index = 0
    comparing_index = 0
    while starting_index < len(array_to_sorted) - 1:
        if comparing_index > len(array_to_sorted) - 1:
            starting_index += 1
            comparing_index = starting_index + 1

        elif array_to_sorted[starting_index] > array_to_sorted[comparing_index]:
            temp = array_to_sorted[starting_index]
            array_to_sorted[starting_index] = array_to_sorted[comparing_index]
            array_to_sorted[comparing_index] = temp

        elif array_to_sorted[starting_index] <= array_to_sorted[comparing_index]:
            comparing_index += 1
    return array_to_sorted


array = [2,4,65,1,5,34]

print(sortingAlgo(array))






