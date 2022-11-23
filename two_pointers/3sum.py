"""
The problem is to find triplets that sum up to 0 where the index of a < b< c and a + b + c = 0 .
the problem can be reduced to twosum problem that is finding a pair of two numbers that sum up to target
if a + b + c = 0 => a + b = -c
how to solve
1. first sort the input array which takes O(NlogN)
2. iterate through the sorted array and if you are at the ith index, find a pair of numbers that add up to
negative of the ith number . to find the two numbers use left and right pointers. if their sum is equal to
negative of the ith number append the ith number and the two pairs to our result array. if their sum is greater
decrement the right pointer by one else if  their sum is less than, then increment the left pointer to
the right.
3. if there are duplicates in the array we don't need to append in the result array. so if the element before
ith element except index 0 is similar to the ith element increment i by one or just continue  and if the
element before the right element is same just decrement right index by one and if the element after the left
pointer is same increment left pointer by one whenever left < right
nums = [-1,0,1,2,-1,-4]  => [-4,-1,-1,0,1,2]

"""


def threeSum(nums):
    nums.sort()
    output = []
    for i in range(len(nums) - 2):
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > -1 * nums[i]:
                right -= 1
            elif nums[left] + nums[right] < -1 * nums[i]:
                left += 1
            else:
                output.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left - 1] == nums[left] and left < right:
                    left += 1

    return output


print(threeSum([-1, 0, 1, 2, -1, -4]))
