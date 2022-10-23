""""
The problem is implementing stack and also finding the minimum value from the stack
we implement the following functions
1. push a value to the stack
2. popping the top of the stack
3. finding the top of the stack
4. get the minimum of the stack
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value):
        self.stack.append(value)
        minimum = min(value, self.minStack[-1] if self.minStack else value)
        self.minStack.append(minimum)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
st = Stack()
st.push(3)
st.push(2)
st.push(4)
print(st.getMin())