"""
The problem is to find the longest substring that is all its elements are increasing order
nums = [1,2,3,2,7]
if the nums array is not empty by default the substring array with length 1 is minimum substring that is in
inceasing order
start i = 0 and j =1, if jth element is greater than its previous element then increament j by one else
max_substring = max(max_substring,j-i) and take i = j and j by 1
terminate the loop when j = len(nums)

"""


def longestIncreasing(nums):
    i = 0
    j = 1
    max_substring = 0
    while j < len(nums):
        if nums[j] >= nums[j - 1]:
            j += 1
            if j == len(nums):
                max_substring = max(max_substring, j - i)
        else:
            max_substring = max(max_substring, j - i)
            i = j
            j += 1
    return max_substring
print(longestIncreasing([6,5,4,1]))
