# def InsertionSort(array):
#     b = 1
#     array_length = len(array)
#     if array_length <= 1:
#         return array
#     while b <= array_length-1:
#         if array[b-1] > array[b]:
#             array[b], array[b-1] = array[b-1], array[b]
#             if b-1 > 0:
#                 b -= 1
#             else: b += 1
#         elif array[b-1] <= array[b]:
#             b += 1
#
#     return array
#
#
#
#
#
#

# class Solution:
#     def insert(self, alist, index, n):
#         return alist
#
#
#     # Function to sort the list using insertion sort algorithm.
#     def insertionSort(self, array, n):
#         b = 1
#         array_length = len(array)
#         if array_length <= 1:
#          return array
#
#         while b <= array_length - 1:
#             if array[b - 1] > array[b]:
#                 array[b], array[b - 1] = array[b - 1], array[b]
#                 if b - 1 > 0:
#                     b -= 1
#                 else:
#                     b += 1
#             elif array[b - 1] <= array[b]:
#                 b += 1
#
#         return array
#
#

def whileCondition(array, index):
    if index > 0 and array[index -1] > array[index]:
        return True
    return False

def insertionSort(array):
    for i in range(len(array)):
        j = i
        while whileCondition(array,j):
            print(array[j - 1], array[j], array[j - 1] > array[j])
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1

    return array


my_array = [64, 34, 25, 12, 22, 11, 90, 5]


print(insertionSort(my_array))



