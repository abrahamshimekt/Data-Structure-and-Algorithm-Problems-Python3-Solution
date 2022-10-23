"""
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
       [10,6,12,-11,*,/,*,17, +,5,+]
       [10,6,-132,/,*,17,+,5,+]
       [10,0,*,17,+,5,+]
       [0,17,+,5,+]
       [17,+,5,+]
       [17,5,+]
       [22]
    we can implement this question using stack
i = 12
stack = [17,5]
"""
from operator import add, sub, mul, truediv


# def evalRPN( tokens):
#     stack = []
#     operators = "+-*/"
#     i = 0
#     while i < len(tokens):
#         while stack and i < len(tokens) and tokens[i] in operators:
#             if len (stack) > 1:
#                  num1 = stack.pop()
#                  num2 = stack.pop()
#                  if tokens[i] == "/":
#                      if abs(num1) > num2:
#                          stack.append(0)
#                      stack.append(num2//num1)
#                  elif tokens[i] == "+":
#                      stack.append(num2 + num1)
#                  elif tokens[i] == "-":
#                      stack.append(num2 - num1)
#                  else:
#                      stack.append(num2 * num1)
#             i +=1
#         else:
#             if i < len(tokens):
#                 stack.append(int(tokens[i]))
#         i +=1
#     return stack[0]



def evalRPN( tokens) :
    operators = {"+": add, "-": sub, "*": mul, "/": truediv}
    stack = []
    for token in tokens:
        if token in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(int(operators[token](operand2, operand1)))
        else:
            stack.append(int(token))
    return stack[0]
print(evalRPN(["4","-2","/","2","-3","-","-"]))
