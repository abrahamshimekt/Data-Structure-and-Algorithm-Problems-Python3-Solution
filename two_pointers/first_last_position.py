"""
The problem is to find the starting and ending position of a target from a given sorted array which is
in ascending order
nums = [5,7,7,8,8] target = 5
we can use two pointers to find the starting and ending position of the target
"""


def firstLastOfTarget(nums, target):
    if target not in nums:
        return [-1, -1]
    i = j = 0
    while i < len(nums) and j < len(nums):
        if nums[j] < target:
            i += 1
            j += 1
        elif nums[j] > target:
            return [i, j - 1]
        else:
            j += 1
            if j == len(nums):
                return [i, j - 1]


print(firstLastOfTarget([5, 7, 7, 8],8 ))
