import random


class NumArray:

    def __init__(self, nums):
        self.prefix_sum = [nums[0]]
        for i in range(1,len(nums)):
            self.prefix_sum.append(self.prefix_sum[i-1] + nums[i])
    def sumRange(self, left: int, right: int) -> int:
        if left>0:
            return self.prefix_sum[right]-self.prefix_sum[left-1]
        return self.prefix_sum[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
print(random.choices([0,1],weights = [4/20,16/20],k=1))