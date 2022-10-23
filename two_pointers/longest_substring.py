"""
The problem is to find a max length substring with all unique characters
s = "abcabcbb"
The bruteforce approach is to use a nested for loop that is O(N^2)
"""


def bruteForce(s):
    ans = ""
    i = 0
    while i < len(s): #O(N)
        j = i + 1
        while j < len(s): #O(N)
            if s[j] == s[i]:
                if len(s[i:j]) > len(ans):
                    ans = s[i:j]
                break
            j += 1
        i += 1
    return len(ans)

#print(bruteForce("pwwkew"))

""" 
let us comeup with a new solution that reduces the time complexity with O(N)
we can use equdirectional two two pointer to solve this problem 
s = "abcabc"
"""
def lengthOfLongestSubstring(s):
    if len(s) == 0 or len(s) == 1:
        return len(s)
    non_repeated = {s[0]:0}
    i,j= 0,1
    max_length = 0
    while i <len(s) and j <len(s):
        if s[j] not in non_repeated:
            non_repeated[s[j]] = 0
            j +=1
            if j==len(s):
                max_length = max(max_length, len(non_repeated))
        else:
            max_length = max(max_length,len(non_repeated))
            non_repeated.pop(s[i])
            i +=1
    return max_length
print(lengthOfLongestSubstring("au"))
