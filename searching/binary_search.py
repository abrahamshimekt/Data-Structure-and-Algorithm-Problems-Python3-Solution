"""
A binary search is an algorithm used to find given item in O(logN) time complexity if the array is already sorted
how to implement binary search
1. find the middle element and compare it with the number to find,if the number to find is greater than
the middle element take the right of the middle element array to search the target element else take the
left of the middle element.
[4,5,6,7,8] ,7
"""


def binarySearch(nums, target):
    mid = len(nums) // 2
    if nums[mid] == target:
        return True
    elif nums[mid] > target:
        return binarySearch(nums[:mid], target)
    else:
        return binarySearch(nums[mid + 1:], target)


print(binarySearch([4, 5, 6, 7, 8], 7))
