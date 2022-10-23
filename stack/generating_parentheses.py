"""
 The problem is to find the possible arrangement of valid parentheses from the given number of parentheses
 for example let n = 2
 parentheses = () ()
 the possible arrangement are:
 ()() , (())
 It can be solved by the following principle recursively
base case:
 openNum == closedNum == n
 output.append("".join(stack))
 return 
"""
