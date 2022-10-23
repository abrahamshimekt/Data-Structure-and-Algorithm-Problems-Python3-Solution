"""
the problem is to find the maximum number of vowels in a substring(contigious part of a string) with k length
s= "baoacb"
k = 3
"""
def max_vowels(s, k):
    vowels = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}
    count = 0
    for i in range(k): # O(k)
        if s[i] in vowels:
            count += 1
    max_count = count
    i = 1
    while i + k <= len(s): # O(N)
        if s[i - 1] in vowels:
            count -= 1
        if s[i + k - 1] in vowels:
            count += 1
        max_count = max(max_count, count)
        i += 1
    return max_count
"""
the total time complexity is O(K + N)  = O(N) and space complexity almost O(1)
"""
print(max_vowels("bacacbefaobeacfe",5))