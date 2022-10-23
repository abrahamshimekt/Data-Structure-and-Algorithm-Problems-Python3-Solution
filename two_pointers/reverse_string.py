"""
The problem is to find the reversed array of strings
the bruteforce approach is to create another array and append all the elements of the old array from its end
to the new array then old array = newarray
but we can use two pointer for in place swapping
["h","e","l","l","o"]
["o","e","l","l","h"]
["o","l","l","e","h"]
"""
def reverseString(s):
    i ,j = 0,len(s)-1
    while i < j:
        s[i],s[j] = s[j],s[i]
        i +=1
        j -=1
    return s
print(reverseString( ["h","e","l","l","o"]))