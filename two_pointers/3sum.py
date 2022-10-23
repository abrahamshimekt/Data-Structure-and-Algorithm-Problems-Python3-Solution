"""
The problem is to find the first 3 numbers that num to zero
nums = [-1,0,1,2,-1,-4]
nums_sorted = [-4,-1,-1,0,1,2]
dictionary = {-4:1,-1:1,1:1,2:1}
-4 + 2 + c= 0
c = -1*nums[i] + (-1* nums[j]) = 2 in dictionary and dictionary[2] != i and dictionary[2] != j
"""


def threeSum(nums):
    nums_sorted = sorted(nums)
    nums_index = {}
    output = []
    for i in range(len(nums_sorted)):
        if nums_sorted[i] not in nums_index:
            nums_index[nums[i]] = i
    i, j = 0, len(nums_sorted) - 1
    while i < j:
        third_num = -1 * nums_sorted[i] + (-1 * nums_sorted[j])
        if third_num in nums_index and (num != i and nums_index[third_num] != j):
            output.append([nums_sorted[i], nums_sorted[j], third_num])
        if third_num > 0:
            i += 1
        else:
            j -= 1
