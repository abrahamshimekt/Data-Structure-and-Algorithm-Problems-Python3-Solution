"""
The problem is to find the number of sub arrays(contiguous part of an array) sum which is equal to zero
[1, 4, -2, -2, 5,-4,3] this array has n(n+1)/2 sub arrays which is 10
[1]
[1,5,3,1,6,2,5] target = 2
[0:2,1:2,5:1,3:2,6:1,2:1]
This problem can be solved by a prefix sum algorithm which says that if we find the sum - target in our prefix
array more than once or if it is repeated we can think that there must be a sum that is a target between the repeated sums
or if the sum - target is zero we have our target sum . It is like a projectile
The bruteforce approach to solve the above question is to use a nested loop and find all subarrays and sum them.
that will be TLE for large input.
"""


def sumZero(nums, target):
    prefix_sum = {0: 1}
    i = 0
    running_sum = 0
    num_subarrays = 0
    while i < len(nums):
        running_sum += nums[i]
        if running_sum - target in prefix_sum:
            num_subarrays += prefix_sum[running_sum - target]
        if running_sum in prefix_sum:
            prefix_sum[running_sum] += 1
        else:
            prefix_sum[running_sum] = 1
        i += 1
    return num_subarrays


print(sumZero([1, 4, -2, -2, 5, -4, 3], 0))
