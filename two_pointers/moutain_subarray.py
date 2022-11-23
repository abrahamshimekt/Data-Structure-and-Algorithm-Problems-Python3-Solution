"""
The problem is to find a mountain subarray such that: if there is index i in that there are exist some
elements before the element in the current index greater than the current element and the  exist some
elements after i which are less than the ith element, then we say that the subarray is a mountain subarray
and then we will compare its its length with current maximum mountain subarray if it is greater than the curre
t we will take it.
how to implement:
1. use two pointers i and j where i started from zero and j from 1
2.  cases:
1 .if nums[j-1] > nums[j] and nums[j+1] > nums[j]: no we need to move both pointers to the right
2. if nums[j-1] > nums[j] and nums[j+1] < nums[j]: yes we can move j to the right by one fixing i at
its current position
3. if nums[j-1] < nums[j] and nums[j+1] > nums[j]: yes we can move j to the right by one fixing i at
its current position
4. if nums[j-1] < nums[j] and nums[j+1] < nums[j]: yes we can move j to the right by fixing i at its current
position
 arr = [0,1,0,4,7,3,2,5]
 i = 1
 j = 5

"""


def longestMountain(arr):
    i, j = 0, 1
    sub_array = 0
    while j < len(arr) - 1:
        if arr[j - 1] > arr[j] and arr[j + 1] > arr[j]:
            sub_array = max(sub_array, j - i + 1)
            i = j
            j += 1
        elif arr[j - 1] > arr[j] > arr[j + 1]:
            j += 1
        elif arr[j - 1] < arr[j] < arr[j + 1]:
            j += 1
        elif arr[j - 1] < arr[j] and arr[j + 1] < arr[j]:
            j += 1
        else:
            i += 1
            j += 1
    return sub_array


print(longestMountain([0, 1, 0]))
