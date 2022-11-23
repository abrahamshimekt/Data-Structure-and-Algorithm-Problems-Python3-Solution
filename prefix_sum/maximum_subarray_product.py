"""
The problem is to find the maximum product subarray.
How to solve:
This problems seems solved by kadanes algorithm which is a ways of finding the maximum subarray sum by keep
tracking the maximum sum so far and the current sum and if the current sum is less than zero update the curr
sum with zero. but to solve this problem we need to consider the current maximum and and the current min
will be swapped if the current element is negative.
so the pseudocode goes like the following ways:
max product so far found = nums[0]
the current max product = nums[0]
the current min product = nums[0]
for(i=1,i < nums.length,i++):
if the nums[i] < 0:
swap(curr_max_product,curr_min_product)
curr max product = max(curr max prodcut * nums[i], nums[i])
curr min product = min(curr min product *nums[i], nums[i])
the ans = max(currmaxproduct,ans)
finally when the loop terminates return the ans
"""
def maxProduct( nums) -> int:
    ans = nums[0]
    max_product =nums[0]
    min_product = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] <0:
            max_product,min_product = min_product,max_product
        max_product = max(max_product*nums[i],nums[i])
        min_product = min(min_product*nums[i],nums[i])
        ans = max(ans,max_product)
        i +=1
    return ans
print(maxProduct([-3,-1,-1]))
