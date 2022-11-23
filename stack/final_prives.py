"""
The problem is to find an array of the final price that someone pay for the ith item
approach:
take the ith item on the top of a stack if there is an item on the right that is less than the element on the
top of the stack take the difference and append the difference at the elements at the top of the stack
index if the element is greater than the element at the top of the stack append it to the top of the stack
prices = [8,4,6,2,3]
ans = [4,2,4,0,0]
st = [[2,3],[3,4]]
"""


def finalPrice(prices):
    n = len(prices)
    answers = [0] * n
    stack = []
    i = 0
    while i < n:
        while stack and stack[-1][0] > prices[i]:
            price, indx = stack.pop()
            answers[indx] = price - prices[i]
        stack.append([prices[i], i])
        i += 1
    for remain in stack:
        answers[remain[1]] = remain[0]
    return answers
print(finalPrice([8,4,6,2,3]))
