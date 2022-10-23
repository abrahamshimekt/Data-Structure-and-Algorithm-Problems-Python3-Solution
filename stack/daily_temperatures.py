"""
The problem says that how many days someone wait to get a warmer temperature from the current day
if today is 71 how many days to wait to get temperature greater than 71. so for each day we need to find a temperature
greater than it. if we do not find a temperature greater than the current day, there will be 0 days
temperatures = [30,40,50,60)
The bruteforce approach is like following and it takes O(N*N) time complexity and O(N) space complexity
"""


def bruteForce(temperatures):
    days_to_wait = []
    for i in range(len(temperatures) - 1):
        warmer = False
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                warmer = True
                days_to_wait.append(j - i)
                break
        if not warmer:
            days_to_wait.append(0)
    days_to_wait.append(0)
    return days_to_wait


print(bruteForce([73, 74, 75, 71, 69, 72, 76, 73]))
"""
How to come up with a better solution with O(N) Time complexity
we can use stack to solve this problem 
"""


def dailyTemperature(temperatures):
    days_to_wait = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and stack[-1][0] < t:
            stackT, indx = stack.pop()
            days_to_wait[indx] = i - indx
        stack.append([t, i])
    return days_to_wait


print(dailyTemperature([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
