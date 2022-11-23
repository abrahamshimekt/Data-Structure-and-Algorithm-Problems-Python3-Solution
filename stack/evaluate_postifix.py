"""The problem is to evalue an experssion given a string with mathematical operators
How to solve:
append  if the current character is a digit and whenever the current character is an operator pop the top
2 numbers and apply the operator on them and append the result at the top of the stack
if the current element is an operator and the stack is empty move to the next
if the current element is  operator and the stack is not empty we will pop the top two elements
else just append the stack
"""


def evalueExpersion(s):
    stack = []
    operators = "+-*/"
    i = 0
    while i < len(s):
        if s[i] in operators and not stack:
            i += 1
        elif s[i] in operators and stack:
            x = stack.pop()
            y = stack.pop()
            if s[i] == "/":
                stack.append(y // x)
            elif s[i] == "-":
                stack.append(y - x)
            elif s[i] == "*":
                stack.append(y * x)
            elif s[i] == "+":
                stack.append(y + x)
            i += 1
        else:
            stack.append(int(s[i]))
            i += 1
    return stack[0]


print(evalueExpersion(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
