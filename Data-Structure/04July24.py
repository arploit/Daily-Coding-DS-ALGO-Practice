# def frequencyCount( arr, N , P):
#     hashmap = {}
#     for value in arr:
#         if not hashmap.get(value):
#             hashmap[value] = 1
#         else:
#             hashmap[value] += 1
#
#     for idx in range(len(arr)):
#         if not hashmap.get(idx+1):
#             print(0, end=" ")
#         else:
#             print(hashmap.get(idx+1), end=" ")


# Function to count the frequency of all elements from 1 to N in the array.

# def frequencyCount( arr, N, P):
#     hashmap = {}
#     for value in arr:
#         if not hashmap.get(value):
#             hashmap[value] = 1
#         else:
#             hashmap[value] += 1
#
#     for idx in range(len(arr)):
#         if not hashmap.get(idx + 1):
#             print(0, end=" ")
#         else:
#             print(hashmap.get(idx + 1), end=" ")
#
#
# frequencyArray = [2,3,2,3,5]
# frequencyCount( frequencyArray, 5, 5)


# Without hashmap


def frequencyCount(arr, N, P):
    i = 0
    while i < N:
        if arr[i] > 0:
            current_value = arr[i]
            if current_value <= N:
                if arr[current_value - 1] < 0:
                    arr[current_value - 1] -= 1
                    arr[i] = 0
                else:
                    temp_value = arr[current_value - 1]
                    arr[current_value - 1] = -1
                    if arr[i] > 0:
                        arr[i] = temp_value
            else:
                arr[i] = 0
                i +=1

        else:
            i += 1
    for i in range(len(arr)):
           arr[i] = arr[i] * -1

    return arr


# frequencyArray = [8,9]
# frequencyArray = frequencyCount(frequencyArray, 2, 5)
frequencyArray = [2,3,2,3,5]
frequencyArray = frequencyCount(frequencyArray, 5, 5)
print(frequencyArray)
