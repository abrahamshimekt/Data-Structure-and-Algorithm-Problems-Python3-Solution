"""
Given a string s,
 check if it can be constructed by taking a substring of it
  and appending multiple copies of the substring together.
  s = "abab"
"""
from collections import Counter


def repeatedSubstringPattern(s):
    i,j=0,1
    seed = ""
    temp = s[0]
    while i < len(s) and j <len(s):
        if s[j] != s[i] :
            temp += s[j]
            j +=1
            if seed !=temp and j==len(s):
                return False
        else:
            if i == 0:
                seed = temp
            elif seed != temp:
                return False
            i = j
            j += 1
            temp = s[i]
            if temp != seed and j == len(s):
                return False

    return True

print(repeatedSubstringPattern("ab"))