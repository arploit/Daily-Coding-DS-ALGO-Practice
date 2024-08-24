# def bubbleSort(array_to_sort):
#     for items in range(len(array_to_sort)-1):
#         index = 0
#         for index_to_update in range(len(array_to_sort) - 1):
#             if array_to_sort[index] <= array_to_sort[index + 1]:
#                 index += 1
#
#             else:
#                 array_to_sort[index] = array_to_sort[index] + array_to_sort[index + 1]
#                 array_to_sort[index + 1] = array_to_sort[index] - array_to_sort[index + 1]
#                 array_to_sort[index] = array_to_sort[index] - array_to_sort[index + 1]
#
#
#     return array_to_sort
#
#
# array = [3,1,64,22,7,90,12]
#
# print(bubbleSort(array))


#
# def bubble_sort(array):
#     array_length = len(array)
#     for item in range(array_length ):
#         swapped = False
#
#         for j in range(array_length - item - 1):
#             if array[j] > array[j + 1]:
#                 array[j] , array[j+1] = array[j+1], array[j]
#                 swapped = True
#
#         if not swapped:
#             break
#
#
#     return array
#
#
# array = [3,1,64,22,7,90,12]
#
#
# print(bubble_sort(array))
                 