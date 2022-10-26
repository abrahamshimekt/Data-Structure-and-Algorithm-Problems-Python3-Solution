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


print(maxSubarraySum([-2, -3, 4, -1, -2, 1, 5, -3]))
