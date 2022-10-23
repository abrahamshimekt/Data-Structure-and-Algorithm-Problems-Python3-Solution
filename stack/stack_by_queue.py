"""
queue is a data structure which works by in principle of first in first out manner
[3,4,5] [3,4] [5] [3,4]
"""
class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self,data):
        self.queue1.append(data)
    def pop(self):
        for i in range(len(self.queue1)-1):
            self.queue2.append(self.queue1.pop(0))
        temp = self.queue1.pop()
        for i in range(len(self.queue2)):
            self.queue1.append(self.queue2.pop(0))
        return  temp
    def top(self):
        return self.queue1[-1]
    def isEmpty(self):
        return len(self.queue1) ==0
s = Stack()
s.queue1 = [3,4,5,6]
s.push(0)
print(s.pop())
from collections import deque
class Stack(object):
    def __init__(self):
        self.q = deque()
    def push(self,data):
        self.q.append(data)
    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()
    def top(self):
        return self.q[-1]
    def isEmpty(self):
        return len(self.q) == 0
