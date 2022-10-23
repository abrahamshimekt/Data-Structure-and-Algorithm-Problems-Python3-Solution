"""
The idea of the problem is to find a substring that sum to the target number then return it
we will sum the first k elements if there sum is less than equal to target and once there sum is
greater than the target we will shrink the window from the left and derement the sum by the one deleted
from our window
{2, 6, 0, 12, 7, 8}, target = 1
"""


def findSubList(nums, target):
    total = nums[0]
    i = 0
    j = 0
    while j < len(nums):
        if total < target:
            j += 1
            total = total + nums[j]
        elif total == target:
            return nums[i:j + 1]
        else:
            total = total - nums[i]
            i += 1
    return []


print(findSubList([2, 6, 0, 12, 7, 8], 0))
