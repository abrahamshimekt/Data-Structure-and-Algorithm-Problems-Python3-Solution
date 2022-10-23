"""
first create a dictionary to check the given parenthesis was closed or not
create a stack which a ds that works in lifo
then iterate through the string and if the
stack is not empty and the last item of the stack is equal to the value of the key from the string:
if the above condition true then pop the top element of the stack else just append the parenthesis to the stack
then finally if when the loop terminates return true if the length of the stack is zero else false
"""
def valid_parenthesis(s):
    parenthesis = {"}":"{",")":"(","]":"["}
    stack = []
    for c in s:
        if stack and stack[-1] == parenthesis.get(c):
            stack.pop()
        else:
            stack.append(c)
    return len(stack) ==0
"""
s = "{[]]()}
stack = ["{","]","}"]
"""
print(valid_parenthesis("([][])"))