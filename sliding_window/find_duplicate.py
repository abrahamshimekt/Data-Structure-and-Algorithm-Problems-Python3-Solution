"""
The problem is to check if there is in a duplicate for the first k elements
take i and j where i =0 and j =1 then check the difference between j and i is <= k:if it is then check the ith and jth element are the same : if the are return found :else increment j by 1
     nums = [5, 6, 5, 2],k = 2
"""
def duplicateFound(nums, k):
    if k > len(nums):
        k = len(nums)
    i, j = 0, 1
    while i + k <= len(nums):
        if j - i <= k:
            if j < len(nums):
                if nums[j] == nums[i]:
                    return True
            else:
                return False
            j += 1
        else:
            i += 1
print(duplicateFound([1, 2, 3, 2, 1],2))