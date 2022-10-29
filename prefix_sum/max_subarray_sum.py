"""
The problem is to find the maximum sum of a subarray for the given array
[-2,-3,4,-1,-2,1,5,-3]
Kadane's Algorithm is used to maintain the maximum sum till the current position
and the maximum sum of the subarray found so far.
"""


def maxSubarraySum(nums):
    current_max = 0
    max_sum = float("-inf")
    i = 0
    while i < len(nums):
        current_max += nums[i]
        if max_sum < current_max:
            max_sum = current_max
        if current_max < 0:
            current_max = 0
        i += 1
    return max_sum


print(maxSubarraySum([-2, -3, 4, -1, -2, 1, -3]))


def maxSubarraySumPrinting(nums):
    curr_max = 0
    max_sum = float("-inf")
    i = 0
    start = end = 0
    move = 0
    while i < len(nums):
        curr_max += nums[i]
        if max_sum < curr_max:
            max_sum = curr_max
            start = move
            end = i
        if curr_max < 0:
            curr_max = 0
            move = i + 1
        i += 1
    return [start, end]


print(maxSubarraySumPrinting([-2, -3, 4, -1, -2, 1, -3]))

"""The above problem can be also solved by prefix sum 
The formula for the max_sum is :
max(max,prefix_sum[i]-min_prefix_sum)
min_sum is :
min(min_prefix_sum,prefix_sum[i])
[-2, -3, 4, -1, -2, 1,5 -3]
prefix_sum = [-2,-5,-1,-2,-4,-3,2,-1]
i = 7
max_sum = 7
min_prefix_sum = -5
"""


def maxSumPrefix(nums):
    min_prefix_sum = 0
    max_sum = float("-inf")
    prefix_sum = [nums[0]]
    for i in range(1, len(nums)):
        prefix_sum.append(prefix_sum[i - 1] + nums[i])
    for i in range(len(nums)):
        max_sum = max(max_sum, prefix_sum[i] - min_prefix_sum)
        min_prefix_sum = min(min_prefix_sum, prefix_sum[i])
    return max_sum


print(maxSumPrefix([-2, -3, 4, -1, -2, 1, 5, -3]))
