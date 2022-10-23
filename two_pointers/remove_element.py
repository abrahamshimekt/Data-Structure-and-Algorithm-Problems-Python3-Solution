"""Given an integer array nums and an integer val,
 remove all occurrences of val in nums in-place.
  The relative order of the elements may be changed.
  The final array should have non val elements
  nums = [3,2,2,3], val = 3
  brute force approach will take O(N^2) because when we remove the ith element == val: all the elements will
  shift to the right which is O(N) worst case.
  but we can use two pointers i and j in opposite direction
  """
def removeElement(nums,val):
    i,j = 0, len(nums)-1
    while i <= j:
        if nums[j] == val:
            j -=1
        elif nums[i] == val:
            nums[i],nums[j] = nums[j],nums[i]
            i +=1
        else:
            i +=1
    return i
print(removeElement([3,3,4],3))

