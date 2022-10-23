"""
 The problem is to find two numbers that add up to a target number
 nums = [2,4,5,9,11,15], target = 12
 brute force approache is
 [2,4],[2,5],[2,7],[2,11],[2,15]
 [4,5],[4,7],[4,11],[4,15]
 [5,7],[5,11],[5,15]
 [7,11],[7,15]
 [11,15]
 r = 5
 l = 0
 while i != j:
 nums[i] + nums[j] > target:
   r -=1
 elif nums[i] + nums[j] == target:
    return [nums[i],nums[j]]
 else:
    l +=1
return []
"""
def twoSum(nums,target):
    r = len(nums)-1
    l = 0
    while l < r:
        if nums[l] + nums[r] > target:
            r -= 1
        elif nums[l] + nums[r] == target:
            return [l, r]
        else:
            l += 1
    return []
print(twoSum([2,1,11,15],9))