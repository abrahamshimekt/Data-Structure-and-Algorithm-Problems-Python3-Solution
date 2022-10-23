def quicksort(arr):
    n = len(arr)
    if n < 2:
        return arr
    curr_pos = 0 # partitioning point
    for i in range(1,n):
        if arr[i] <= arr[0]:
            curr_pos +=1
            arr[i],arr[curr_pos] = arr[curr_pos],arr[i]
    arr[0],arr[curr_pos] = arr[curr_pos],arr[0]
    return quicksort(arr[0:curr_pos]) + [arr[curr_pos]] + quicksort(arr[curr_pos+1:n])
print(quicksort([6,2,9,7,1]))

def selectionsort(arr): # works by every time selecting the minimum element
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i +1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
print(selectionsort([6,2,9,7,1]))

def insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        curr_val = arr[i]
        curr_pos = i
        while curr_pos > 0 and arr[curr_pos-1] > curr_val:
            arr[curr_pos] = arr[curr_pos-1]
            curr_pos -=1
        arr[curr_pos] = curr_val
    return arr
print(insertionsort([6,2,9,7,1]))
def insertionsort2(arr):
    for i in range(1,len(arr)):
        value_to_sort = arr[i]
        while arr[i-1] > value_to_sort and i>0:
            arr[i-1],arr[i] = arr[i],arr[i -1]
            i -=1
    return arr
print(f"insertion:{insertionsort2([7,2,6,1,8])}")
def mergesort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    mergesort(left)
    mergesort(right)
    i=j=k = 0
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
print(f"merge:{mergesort([4,51,2,1,9])}")
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j +1]:
                arr[j],arr[j +1] = arr[j+1],arr[j]
    return arr
print(f"bubble:{bubblesort([9,6,3,2,5])}")
def bubblesort2(arr):
    indx = len(arr)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(indx):
            if arr[i] > arr[i +1]:
                sorted = False
                arr[i],arr[i +1] = arr[i+1],arr[i]
    return arr

print(f"bubble2:{bubblesort2([5,6,1,7])}")
def ts(arr):
    if len(arr) == 1:
        return arr[0]
    new_arr = []
    for i in range(len(arr)-1):
        new_arr.append((arr[i] + arr[i + 1])%10)
    return ts(new_arr)
print(ts([1,]))
def ds(s,k):
    if len(s) <= k:
        return s
    i =0
    j = 1
    new_s = ""
    while i < len(s):
        new_s += f"{sum([int(x) for x in s[i:k*j]])}"
        i +=k
        j +=1
    return ds(new_s,k)
print(ds("11111222223",3))




