"""
quick sort works as the following
1. start from the pivot where i = 0
2. iterate from ith + 1 to the end and if there is an element
that is less than or equal to the first element ,change the current
 postition and swap the ith element and the current pos element
3. when the loop terminates swap the first element and the current pos element
4. call quick_sort(arr[:current_pos]) and call quick_sort(arr[current_pos:])
5. merge quick_sort(arr[0:current_pos]) + arr[current_pos] and quick_sort(arr[current_pos+1:])

"""
def quick_sort(arr):
    n= len(arr)
    if n < 2:
        return arr
    pivot = 0
    for i in range(1,n):
        if arr[i] <= arr[0]:
            pivot +=1
            arr[i],arr[pivot] = arr[pivot],arr[i]
    arr[0],arr[pivot] = arr[pivot],arr[0]
    return quick_sort(arr[:pivot]) + [arr[pivot]] + quick_sort(arr[pivot+1:])
print(f"quick:{quick_sort([3,6,1,8])}")

