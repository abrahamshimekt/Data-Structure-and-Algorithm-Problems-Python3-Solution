"""
first iterate through the nums array by slicing the array from current position of i to i + k
then find the max element from the sliced array from the nums array by moving i by one position to the right
append the max element to our out put array
final loop terminated when i + k > len(nums)
"""
def maxSliding_window(nums,k):
    output = []
    i = 0
    while i + k <= len(nums):
        output.append(max(nums[i:i +k]))
        i +=1
    return output
print(maxSliding_window([1,1,1,1,1,4,5],6))
from collections import  deque
def maxSliding_window2(nums,k):
    output = []
    i ,j= 0,0
    q = deque()
    while j < len(nums):
        while q and nums[q[-1]] < nums[j]:
            q.pop()
        q.append(j)
        if i > q[0]:
            q.popleft()
        if j + 1 >= k:
            output.append(nums[q[0]])
            i +=1
        j +=1
    return output
print(maxSliding_window2([1,1,1,1,1,4,5],6))


