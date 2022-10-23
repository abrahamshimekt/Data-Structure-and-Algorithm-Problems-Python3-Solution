"""
The problem is to find the count of distinict elements in a k length subarray of an array
arr[] = { 0, 1, 2, 3, 2, 1, 4, 5 };
k = 5;
"""
from collections import Counter
def countDistinict(nums,k):
    seed = Counter(nums[:k])
    count = len(seed)
    output = []
    i = 1
    while i + k <= len(nums):
        output.append(count)
        seed[nums[i - 1]] -= 1
        if seed[nums[i - 1]] == 0:
            seed.pop(nums[i -1])
            count -= 1
        if nums[i + k - 1] not in seed:
            seed[nums[i + k - 1]] = 1
            count += 1
        else:
            seed[nums[i + k - 1]] += 1

        i += 1
    output.append(count)
    return output
print(countDistinict([2, 1, 2, 3, 2, 1, 4, 5],5))