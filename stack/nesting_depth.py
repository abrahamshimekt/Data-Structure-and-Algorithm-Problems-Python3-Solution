"""
The problem is to find the maximum nesting depth of the given valid parentheses string
approach:
stack can handle this problem in sophisticated way
first we need to build only parentheses string
then while stack and the top of the stack is match with the closing parentheses ")" we will pop the
"(" from the top of the stack and count the nesting then we will take the maximum nesting.
""
st = [(]
curr = 1
"""


def maxNesting(vps):
    stack = []
    vps_par = ""
    n = len(vps)
    for j in range(n):
        if vps[j] in ")(":
            vps_par += vps[j]
    depth = 0
    parentheses = {")": "("}
    i = 0
    curr_depth = 0
    k = len(vps_par)
    while i < k:
        if stack and stack[-1] == parentheses.get(vps_par[i], None):
            curr_depth += 1
            stack.pop()
            if i + 1 == k:
                depth = max(depth, curr_depth)
        else:
            stack.append(vps_par[i])
            depth = max(depth, curr_depth)
            curr_depth = 0
        i += 1
    return depth

print(maxNesting("(1)+((2))+(((3)))"))
