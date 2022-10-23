"""
The problem is to check if the give string is whether a palindrome or not after doing the following
operation on the string
1 make capital letters to small letter
2. remove numbers and symbols
example s = "A man, a plan, a canal: Panama" s = "amanaplanacanalpanama"
so we need a dictionary to make a check whether the charcter is alphabet or not
for c in s:
if the character is in the aphabet dictionary then we will concatenate to the string we are building:else
continue
after we finish building the string s then we will check if the string is a palindrome or not
so we use opposite direction two pointer technique to compare the first and the last characters : whenever
we find the situation that the ith and jth characters are not equal we will return false immediately.
Lets code it
"""


def validPalindrome(s):
    aplpabets = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
                 "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
                 "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    extracted_string = ""
    for c in s:
        if c.lower() in aplpabets:
            extracted_string += c.lower()
    i = 0
    j = len(extracted_string) - 1
    print(extracted_string)
    while  i < j:
        if extracted_string[i] != extracted_string[j]:
            return False
        i += 1
        j -= 1
    return True
print(validPalindrome( "A man, a plan, a canal: Panama"))
