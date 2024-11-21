def mergeSort(array, low, high):
    if low >= high:
        return
    '''
    Merge Sort is recursive algorithm to sort the array
    This sort use divide and sort method
    
    '''
    # step 1 find a middle ground divide the array
    middle = int((low + high) / 2)
    # step 2. Sort the left most array
    mergeSort(array, low, middle)
    # step 3. sort the right section of array
    mergeSort(array, middle + 1, high)
    # step 4. Once both side is sorted merge them
    merge(array, low, middle, high)


def merge(arr, low, middle, high):
    temp = []  # to store sorted array temporarily
    left = low  # left
    right = middle + 1

    '''
    if left is smaller than or equal to low and right is smaller than or equal to high:
    '''
    while left <= middle and right <= high:
        '''
        check weather arr left is smaller or equal to right 
        then push that element in to temp array and increase that pointer
        '''
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    # Step 2. Once done sorting push all the left and right element into temp array
    while left <= middle:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    # Step 3. Once sorting is done push all the temp array value in to original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]


# newArray = [2, 5, 1, 10, 8, 24]

newArray = [4, 2, 1, 0]
mergeSort(newArray, 0, len(newArray) - 1)
print(newArray)
