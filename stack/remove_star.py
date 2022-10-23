def removeStars(s):
    stack = []
    i = 0
    while i < len(s):
        if s[i] == "*" and i == 0:
            i += 1
        while stack and i < len(s) and s[i] == "*":
            stack.pop()
            i += 1
        if i < len(s) and s[i] != "*" :
            stack.append(s[i])
        i += 1
    return "".join(stack)


print(removeStars("leet**cod*e"))
"""
i = 0
stack = []
i = 1
stack = []
i = 2
stack =[B]
i = 3
stack = [B,B]
i = 4
stack = [B,B,B]
i = 5
stack = [B,B] 
"""
