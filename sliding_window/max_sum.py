"""
first what we just do is finding the first kth elements window sum
then assign this sum to the current_max sum
then we iterate through the array starting from i = 1 and we dreament the previouse element before i from the window sum and k + i
then compare the window to the current sum then assign the current with window
[4,5,7,2,1,8,9], k = 3
window_sum = sum[:k] = 16
current_sum = 16
i = 1
while i + k <= len(nums):
    window_sum = window_sum -nums[i-1] + nums[k+i-1]
    current_sum = max(current_sum,window_sum)
    i +=1
return current_sum
"""
def max_sum(nums,k):
    window_sum = sum(nums[:k])
    current_sum = window_sum
    i = 1
    while i + k <= len(nums):
        window_sum = window_sum - nums[i-1] + nums[k +i -1]
        current_sum = max(current_sum,window_sum)
        i +=1
    return current_sum
print(max_sum([2,3,5,6,7,17,1,0,0,1],4))
