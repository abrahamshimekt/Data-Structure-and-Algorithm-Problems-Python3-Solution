"""
The problem is to move all zeros to the end of an array
nums = [0,1,0,3,12]
[1,0,3,12,0]
[1,3,12,0,0]
what if we use two pointers i = 0 and j = len(nums)-1
i = 0,j= 4
[0,1,0,3,12]
i=0,j=3
[12,1,0,3,0]
i = 2,j=3
[12,1,3,0,0]
"""
