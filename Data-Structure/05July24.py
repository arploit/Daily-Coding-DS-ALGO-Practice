from _ast import List


def maxFrequency(nums, k: int) -> int:
    # i = 0
    # j = 0
    # maxwindowlength = 0
    # nums.sort()
    # total = nums[0]
    # array_length = len(nums)
    # while i < array_length - 1:
    #     current_value = nums[j]
    #     window_length = (j - i)
    #     if current_value * window_length <= (total + k):
    #         if j < (array_length - 1):
    #             j = j + 1
    #         # print(j)
    #         total = nums[i] + nums[j]
    #         # print(total)
    #         if (j - i + 1) > maxwindowlength:
    #             maxwindowlength = j - i
    #     else:
    #         total = total - nums[i]
    #         i = + 1
    # return maxwindowlength
    l,r = 0,0
    res, total = 0,0
    nums.sort()
    while r < len(nums):
        total += nums[r]

        while nums[r] * (r - l + 1) > total + k:
            total -= nums[l]
            l += 1
        res = max(res, r-l+1)
        r += 1

    return res



# nums = [1, 2, 4]
# k = 5

nums = [3,9,2]
k = 2
print(maxFrequency(nums, k))
