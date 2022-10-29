"""
how bubble sort works
1. take an element each iteration and compare it
 to every element in the array and bubble it or swap in its write position
"""


def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


print(f"bubble: {bubble_sort([4, 5, 2, 6])}")


def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


print(bubbleSort([4, 2, 6, 1, 8]))
