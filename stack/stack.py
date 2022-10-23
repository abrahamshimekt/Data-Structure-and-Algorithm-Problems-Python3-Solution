"""
stack is a data structure that works in a fashion of last element is the first element to be removed
"""
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) ==0
    def top(self):
        return self.stack[-1]
stck = Stack()
stck.stack = [3,4,65,1]
stck.push(5)
stck.pop()



print(stck.pop())




