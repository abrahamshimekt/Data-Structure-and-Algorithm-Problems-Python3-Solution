"""
how seleciton sort works is the following ways :
1. the algorithm works by finding the minimum element
2. take the ith element as the minimum element and assign i as the minimum index of the minimum element
compare this minimum element to all elements of from ith + 1 element and if we find the element that is less
than the current element, then we update the min index
3. after comparing of min element to ith + 1 element swap the ith element and the min element
"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
print(f"selection:{selection_sort([4,5,1,6])}")