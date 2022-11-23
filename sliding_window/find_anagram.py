"""
The problem is to find all substrings that are anagram to the target string, and
 then we will append the anagram and its starting position to a list
 then we iterate to the list and print the anagram and the position
 'XYYZXZ' "XYZ"
"""
from collections import Counter

def findAnagram(s, target):
    k = len(target)
    target = Counter(target)
    anagram = Counter(s[:k])
    output = []
    i = 1
    while i + k <= len(s):
        if anagram == target:
            output.append((s[i-1:k + i-1], i-1))
        anagram[s[i-1]] -= 1
        if s[k + i-1] not in anagram:
            anagram[s[k + i-1]] = 1
        else:
            anagram[s[k + i-1]] += 1
        i += 1
    if anagram == target:
        output.append((s[i-1:k + i - 1], i - 1))
    return output
print(findAnagram( 'XYYZXZYZXXYZ', "XYZ"))
