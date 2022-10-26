"""
The problem is to find the minimum length of subarray with sum greater than or equal to target
target = 7, nums =  [1,2,2,3,3,4],7 [1,4,4] 4 [1,1,1,1,1,1,1,1] 11
a-b = c where b is the target which is constant  and a is the sum of the first ith elements and c is the difference that we need to search
on the prefix array
a-7 = c>=7
i = 0
a= 1
1-7 = c = -6 : is there any sum from the array that is -6:No then add the sum to our prefix_sum
prefix_sum = {0:1,1:1}
i= 1
a = 3
3-7=c = -4 : is there any sum from the array that is -4: No then add the sum to our prefix_sum
prefix_sum = {0:1,1:1,3:1}
i = 2
a = 5
5- 7 = c = -2 :No
prefix_sum = {0:1,1:1,3:1,5:1}
i = 5,a = 15,15-7 = c = 8:yes
res = 2,prefix_sum = {0:1,1:2,3:1,5:1,8:2,11:1}

"""


def minSubArrayLen(nums, target):
    prefix_sum = {0: 1}
    running_sum = 0
    i = 0
    result = 0
    while i < len(nums):
        running_sum += nums[i]
        if running_sum - target in prefix_sum:
            result += 1
        if running_sum not in prefix_sum:
            prefix_sum[running_sum] = 1
        else:
            prefix_sum[running_sum] += 1
        i += 1
    return result


print(minSubArrayLen([1, 4, 4], 4))