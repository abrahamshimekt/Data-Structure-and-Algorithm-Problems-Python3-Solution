"""
The problem is to move all zeros to the end of an array
to solve the problem we can use two pointers i and j where i
used to choice a zero element and j to choice
a non-zero element
nums = [1,0,1,0,0]
"""


def moveZeros(nums):
    i, j = 0, 1
    while j < len(nums):
        if nums[i] != 0:
            i += 1
            j += 1
        elif nums[j] == 0:
            j += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
    return nums


print(moveZeros([0, 1, 0, 0, 0]))
