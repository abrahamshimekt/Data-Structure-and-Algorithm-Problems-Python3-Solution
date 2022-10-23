"""
The first thing is to find the minimum price from the prices list
then fix the i pointer at this position and move the j pointer till the end of the prices array
at each position of j find the difference between ith element and jth element
if the difference is greater than the current max_profit then change the current profit by difference
then finally if j > len(nums) terminate the loop
prices = [1,5,3,6,4,7]
min= min(prices) = 1
i ,j = 0,1
profit = 0
while j < len(nums):
    if nums[i] == min:
        if nums[j]-nums[i] > profit:
            profit = nums[j]-nums[i]
        j +=1
    else:
        i +=1
        j +=1


"""
def maxProfit(prices):
    low_price = min(prices)
    profit = 0
    i,j = 0,1
    while j < len(prices):
        if prices[i] == low_price:
            profit = max(profit,prices[j] - prices[i])
            j +=1
        else:
            i +=1
            j +=1
    return profit
print(maxProfit([3,4,6,1,6,7,19,1,20]))
def maxProfit2(prices):
    lp,rp = 0,1
    maxProfit = 0
    while rp < len(prices):
        if prices[lp] < prices[rp]:
            maxProfit = max(maxProfit,prices[rp]-prices[lp])
        else:
            lp = rp
        rp +=1
    return maxProfit
print(maxProfit([3,4,6,1,6,7,19,1,20]))