"""
The problem is to remove consecutive similar characters that are lower case and uppercase
s = "lEeetcode"
i = 7
stack = [l,e,e,t,c,o,d,e]
"""


def makeGood(s):
    stack = []
    i = 0
    while i < len(s):
        while stack and (abs(ord(stack[-1]) - ord(s[i])) == 32 or abs(ord(s[i]) - ord(stack[-1])) == 32):
            stack.pop()
            i += 1
        else:
            if i < len(s):
                stack.append(s[i])
            i += 1
    return "".join(stack)


print(makeGood("a"))
