"""The problem is to check if the permutation of s1 is in s2 that means by taking s1 length of substring
from s2 and check if that portion of string is equal to s1 if that is the case we will return true
else return false
s1 = "ab" s2 = "eidbaooo"
we can use two equi directional pointers i and j where i starts from 0 and j starts from k which the length of s1
i and j increment by 1 and the loop terminates at i + k == len(s2)
"""
from collections import Counter


def permutationString(s1,s2):
    k = len(s1)
    s1_dictionary = Counter(s1)
    i, j = 0,k
    while i + k <= len(s2):
        if Counter(s2[i:j]) == s1_dictionary:
            return True
        i +=1
        j +=1
    return False
print(permutationString("ab","eidboao"))

