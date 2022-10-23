"""
how bubble sort works
1. take an element each iteration and compare it to every element in the array and bubble it or swap in its write positon
"""
def bubble_sort(arr):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i +1]:
                sorted = False
                arr[i],arr[i +1] = arr[i + 1],arr[i]
    return arr
print(f"bubble: {bubble_sort([4,5,2,6])}")
# i = 0, [4,5,2,6]
# i = 1, [4,2,5,6]
# i = 2, [4,2,5,6]
# i = 0, [2,4,5,6]

