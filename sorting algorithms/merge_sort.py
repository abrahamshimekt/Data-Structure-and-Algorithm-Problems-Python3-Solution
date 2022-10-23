"""
how merge sort works
1. first check if the len(arr) less than 2
2. if len(arr) >2 find the mid for paritioning which is half of the length of the array
3. call mergesort on the left of the mid and  the right of the mid point of the parition
4. the merge and the sort algoritm goes like the following
5. assign i, j and k with 0
6. compare the ith and jth values of the left and right arrarys and assign the less element on arr[k]
7. after the comparing of the left and right elements there will be elements left on the left and right array
and add these elements to the array first the left and second the right
"""
def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)
    i = j= k=0
    while i <len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i +=1
        else:
            arr[k] = right[j]
            j +=1
        k +=1
    while i < len(left):
        arr[k] = left[i]
        i +=1
        k +=1
    while j < len(right):
        arr[k] = right[j]
        j +=1
        k +=1
    return arr
print(f"mergesort:{mergesort([4,2,3,6])}")