"""
The problem is to find the number of tuples i, j and k such that i< j< k and nums[i] + nums[j] + nums[k] = target
the permutation of selecting 3 indexes from the total of n objects is n!/(n-3)! => (n-1)(n-2) = n^2 -3n -3
how to solve
1. first sort the array in ascending order
2. take the ith number and find the next two pairs that sum up to target minus the ith number: the problem
can be reduced to two sum by taking left and right pointers. if the sum of the left and the right pointer numbers
greater than the target minus the ith number decrement the right pointer to the left and if the sum is less than,
increment the left pointer to the right else if the sum is equal increase the count by one
 arr = [1,1,2,2,3,3,4,4,5,5], target = 8
"""
from collections import Counter


def threeSumMulti(arr, target):
    freq = Counter(arr)
    res = 0
    n = len(arr)
    i = 0
    while i < n:
        left = i + 1
        right = n - 1
        while left < right:
            if arr[left] + arr[right] < target - arr[i]:
                left += 1
            elif arr[left] + arr[right] > target - arr[i]:
                right -= 1
            else:
                if arr[right] != arr[left] != arr[i]:
                    res += freq[arr[i]] * freq[arr[left]] * freq[arr[right]]
                elif arr[right] == arr[left] != arr[i]:
                    res += freq[arr[right]] * (freq[arr[right]] - 1) * freq[arr[i]] // 2
                elif arr[right] != arr[left] == arr[i]:
                    res += freq[arr[left]] * (freq[arr[left]] - 1) * freq[arr[right]] // 2
                else:
                    res += freq[arr[right]] * (freq[arr[right]] - 1) * (freq[arr[right]] - 2) // 6
                left += freq[arr[left]]
                right -= freq[arr[right]]
            i += freq[arr[i]]
        return res % 1000000007

print(threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
