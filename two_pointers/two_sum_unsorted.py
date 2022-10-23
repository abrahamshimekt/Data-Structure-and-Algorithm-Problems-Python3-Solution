"""
The problem is to find two nums that add up to a given target number.
here the array can not be sorted because
we need to return the place where the two numbers found from the array
The first thing we do is to create a dictionary of the numbers in the array and their position
nums = [2,7,11,15], target = 9
nums_index = {2:0,7:1,11:2,15:3}
the we iterate through the array then we check the diffrence between target and  the ith item is in the
dictionary it is then return the the indexes
"""
def twoSum(nums,target):
    nums_index = {}
    for i in range(len(nums)):
        if nums[i] not in nums_index:
            nums_index[nums[i]] = i
    for i in range(len(nums)):
        if target-nums[i] in nums_index and i != nums_index[target-nums[i]]:
            return [i,nums_index[target-nums[i]]]
print(twoSum([2,7,11,15],9))