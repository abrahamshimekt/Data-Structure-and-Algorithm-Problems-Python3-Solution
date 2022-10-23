"""
The problem is to find the intersection of two arrays, then the intersection must be unique
nums1 = [1,2,2,1], nums2 = [2,2]
the intersection of nums1 and nums2 = [2]
we can change both of them to a set and the find the
intersection of them and change the intersection into  alist
nums1 = {1,2}
nums2 = {2}
output = list(nums1.intersection(nums2))
"""


def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    return list(nums1.intersection(nums2))


print(intersection([4, 9, 5], [9, 4, 9, 8, 4]))

"""
How can this problem be solved using two pointers 

"""

