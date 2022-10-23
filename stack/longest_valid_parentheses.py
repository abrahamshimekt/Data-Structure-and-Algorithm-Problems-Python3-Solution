"""
The problem is to return the length of the longest valid parentheses from a string which contains
only  ) and ( only
valid parenthesis is ()
such kind of problems are solved using stack because it requires matching
s =  "(()"
i = 0
stack = ["("]
i = 1
stack = []
i = 2
stack = ["("]
"""
def longestValidParentheses(s):
    if len(s) == 0:
        return 0
    parenthesis = {")":"("}
    i = 0
    stack = []
    while i < len(s):
        if stack and stack[-1] != parenthesis.get(s[i]):
            stack.pop()
        else:
            stack.append(s[i])
            i +=1
    return len(stack)
print(longestValidParentheses( ")()())"))
