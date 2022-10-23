"""Given two strings needle and haystack,
 return the index of the first occurrence of needle in haystack,
  or -1 if needle is not part of haystack.
  haystack = "butsad", needle = "sad"

"""
def strStr( haystack, needle) :
    k = len(needle)
    i = 0
    while i + k <= len(haystack):
        if haystack[i:k+i] == needle:
            return i
        i +=1
    return -1
print(strStr( "hello","ll"))
