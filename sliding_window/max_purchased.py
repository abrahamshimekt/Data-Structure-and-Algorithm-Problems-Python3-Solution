"""
The solution for the problem is based on the sliding window technique "
sliding window technique works when the window size fixed to reduce the time complexity of the algo
The problem is to find the maximum consecutive elements that follow the following formula
max(cost1) + sum(cost2)*k <= budget where k is the length of the first k elements selected
max and sum are the first k elements that are selected
first thing to do is to find the max window size k the full fill the above scenario
any window size less than k will be ignored
so we use two pointers i and j both start from 0
we move all the ways to that fulfils the above condition then if we find the situation that doesn't full fill:
 we get our window size k. after we find our k then our j will always start from i + k but i increment by 1
 cost1 = [3, 6, 1, 3, 4] cost2 = [2, 1, 3, 4, 5] budget = 25
 sum_ = 0
 k = 0
 i =0,j =1
 max(cost1[i:j])  + sum_ = sum_ + cost2[j-1] = 3 + 2*(j - i) = 5<= 25
 k = max(k,j - i)= 1
 i= 0,j = 2
 max(cost1[i:j])  + sum_ = sum_ + cost2[j-1] = 6 + 3*(j - i) = 12<=25
 k = max(1,2) = 2
 i=0,j=3
 max(cost1[i:j])  + sum_ = sum_ + cost2[j-1] = 6 + 6*(j - i)= 24<=25
  j +=1
 k = max(2,3) = 3
 i= 0,j = 4
max(cost1[i:j]) + sum_ = sum_ + cost2[j-1] = 6 + 10*(j - i) = 46<=25 :
    j +=1
 else:
    i +=1
    j +=1
 i = 1,j = 5
  max(cost1[i:j]) + sum_ = sum_ + cost2[j-1] = 6 + 13*4 = 30<=25 :
else:
 sum_ = sum_ - cost2[i]
 i +=1
 j +=1
 i=2,j = 6 the loop terminates and return k
 let us code this


"""
"""cost1 = [3, 6, 1, 3, 4] cost2 = [2, 1, 3, 4, 5]"""
def maxPurchased(cost1,cost2,budget):
    sum_ = 0
    k = 0
    i,j= 0,1
    while j <= len(cost1):
        sum_ = sum_ + cost2[j-1]
        if max(cost1[i:j]) + (sum_)*(j-i) <= budget:
            k = max(k,j-i)
            j +=1
        else:
            sum_ = sum_ - cost2[i]
            i +=1
            j +=1
    return k
print(maxPurchased([12, 13, 19],[9, 7, 6],18))

