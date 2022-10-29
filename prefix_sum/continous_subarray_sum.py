"""
Given an integer array nums and an integer k,
return true if nums has a continuous subarray of size at least two
 whose elements sum up to a multiple of k, or false otherwise.
An integer x is a multiple of k if there exists an integer
 n such that x = n * k. 0 is always a multiple of k.
 The problem can be solved using prefix sum algorithm
 first assume that an empty subarray is sum up to zero, and it is a subarray of length 0.but our subarray length
 must be greater than or equal to 2.
 we then add the current running sum modulo by k  and the position in our prefix remainder if it is only not existed before
 then we check if  the current position minus prefix_remainder[remainder] >=2: if it is the case we will return true
 [23,2,4,6,7], k = 6
 i = 3
 prefix_remainder = {0:-1,7:0,3:1,1:2}
 prefix_sum = 0
prefix_sum = (prefix_sum + nums[i])%k = 1
"""