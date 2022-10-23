"""
The problem says there is an array of zeros and ones
the task to flip k 0s to 1 and return the maximum length of consecutive ones after flipping k zeros to 1
 ,[1,1,1,1]
i = j = 0
if nums[0] =1==0 and 0 <=2: no flipping and no flipping = 0
nums = [1,0,1,0,0,0,1]
i=0,j = 1
if nums[1]=0==0 and 0 <= k: flipping =1
nums = [1,1,1,0,0,1]
i=0,j =2
if nums[2] = 1==0 and 1<= 2: no flipping =1
nums = [1,1,1,0,0,1,1]
i =0,j =3
if nums[3] =0==0 and 1< 2: flipping = 2
j +=1
nums = [1,1,1,1,0,1]
i = 0,j= 4
if nums[4] = 0==0 and 2<2:no flipping = 2
j +=1
elif nums[j] == 1:
j +=1
else:
    max_ = max(max_,j-i)
    flipping = 0
    i +=1
i = 1,j = 4
if nums[4] =0==0 and 0< 2: flipping = 1
   j +=1
nums = [1,1,1,1,1,0,1]
i = 1,j = 5
if nums[5] = 0==0 and 1< 2:  flipping = 2
j +=1
nums = [1,1,1,1,1,1,1,1]
i =1,j=6
if nums[6] = 1==0 and 2<2:


"""
"""nums = [1,1,1,0,0,1] k = 2,[1,1,1,1,0,1],[1,1,1,1,1,1]"""



def flippingZeros(nums, k):
    max_ = 0
    i = j = 0
    flipping = 0
    while j < len(nums):
        if nums[j] == 0 and flipping < k:
            j += 1
            flipping += 1
        elif nums[j] == 1:
            j += 1
            if j == len(nums):
                max_ = max(max_,j-i)
        else:
            max_ = max(max_, j - i)
            flipping = 0
            i += 1
    return max_
print(flippingZeros([1,1,1,0,0,1],2))
