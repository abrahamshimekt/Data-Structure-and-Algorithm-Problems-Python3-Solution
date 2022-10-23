"""
You are given an array people where people[i] is
the weight of the ith person, and an infinite number of boats
 where each boat can carry a maximum weight of limit. Each boat
 carries at most two people at the same time, provided the sum
 of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person

I think this question can be solved by using two pointers in O(N) time complexity
[3,2,2,1],[1,1,1,3] limit = 3
"""


def numRescueBoats(people, limit):
    num_boats = 0
    stack = []
    i = 0
    while i < len(people):
        if stack:
            if stack[-1] == limit:
                num_boats += 1
                stack.pop()
            elif stack[-1] + people[i] > limit:
                num_boats += 1
                stack.pop()
            else:
                temp = stack.pop()
                stack.append(temp + people[i])
                i += 1
                if stack[-1] == limit and i == len(people):
                    num_boats += 1
        else:
            stack.append(people[i])
            i += 1
            if stack and i == len(people):
                num_boats += 1
    return num_boats


print(numRescueBoats([3, 5, 3, 4], 5))
""" i =0
stack = []
i = 1
stack = [3]
i = 2 
stack = [2]
i = 3
stack = [2]
i = 4
"""
