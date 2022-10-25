"""
Given a sequence arr[] of size n, Write a function int equilibrium(int[] arr,
 int n) that returns an equilibrium index (if any) or -1 if no equilibrium index exists.

The equilibrium index of an array is an index such that the sum of elements at lower indexes
 is equal to the sum of elements at higher indexes.
 how to approach this problem is to use two sums one starting from the beginning and the other from the end
 {-6, 1, 5, 2, -4, 3, 3}
 {1, 2, 3}
 rightsum =[3,6,2,4,9,10,4]
 leftsum = [-6,-5,0,2,-2,1,4]
"""
# def equilibriumIndex(nums):
#     i,j = 0, len(nums)-1
#     leftsum = 0
#     rightsum = 0
#     while i < j :
#         leftsum += nums[i]
#         rightsum +=nums[j]
#         i +=1
#         j -=1
#     if leftsum == rightsum:
#         return i
#     return -1
# print(equilibriumIndex([-6, 1, 5, 2, -4, 3, 3]))
# def equilibrium(nums):
#     total = 0
#     for i in range(len(nums)):
#         total +=nums[i]
#     leftsum = 0
#     for i in range(len(nums)):
#         total -= nums[i]
#         if leftsum == total:
#             return i
#         leftsum += nums[i]
#     return -1
# print(equilibrium([-6, 1, 5, 2, -4, 3, 3]))
"""
using prefix_sum we can implement the problem in the following way
"""


def equilbriumPrefix(nums):
    n = len(nums) - 1
    rightsum = [nums[n]]
    leftsum = [nums[0]]
    for i in range(1, n+1):
        rightsum.append(rightsum[i - 1] + nums[n - i])
        leftsum.append(leftsum[i - 1] + nums[i])
    for i in range(n+1):
        if leftsum[i] == rightsum[n - i]:
            return i
    return -1
print(equilbriumPrefix([1,2,3]))
