"""
 The problem is to find the number of sub arrays that have k odd numbers in it.
 if the ith item is odd increase the count by one until the count is equal to k. if the count is k shrink the window
 to the right if the element left is odd decrement the count by one else just shrink simply.
 nums = [2,2,2,1,2,2,1,2,2,2] and k = 2
 [0,0,0,1,0,0,1,0,0,0]
 [0,0,0,1,1,1,2,2,2,2]
 dico = {0:4,1:3,2:4}
 i=1,j = 5
 ns = 1
 count = 3
"""


def numberOfSubarrays(nums, k):
    remainders = []
    rem = 0
    num_subarray = 0
    for num in nums:
        rem += num % 2
        remainders.append(rem)
    prefix = {0: 1}
    for remainder in remainders:
        if remainder - k in prefix:
            num_subarray += prefix[remainder - k]
        if remainder not in prefix:
            prefix[remainder] =1
        else:
            prefix[remainder] += 1
    return num_subarray

print(numberOfSubarrays([1,1,2,1,1], 3))
