"""
There are a list of asteroids and they will collid in the following principle
1. absolute value of the ith asteroid is its length
2. negative sign shows moving to the left
3. positive sign shows moving to the right
4. all moving in the same speed
5. if the larger collide with the smaller, then the smaller will be destroyed
6. if both asteroids collide have the same size, then both will be destroyed
asteroids = [5,10,-5]
"""
def asteroidCollision2(asteroids):
    stack = []
    for a in asteroids:
        while stack and a < 0 and stack [-1] >0:
            diff = a + stack[-1]
            if diff < 0:
                stack.pop()
            elif diff > 0:
                a = 0
            else:
                a = 0
                stack.pop()
        if a:
            stack.append(a)
    return stack
print(asteroidCollision2([-1,3,2,-3,4]))
def asteroidCollision(asteroids):
    i = 1
    stack = [asteroids[0]]
    while i < len(asteroids):
        if not stack:
            stack.append(asteroids[i])
        elif stack[-1] < 0:
            stack.append(asteroids[i])
            i += 1
        elif stack[-1] > 0 and asteroids[i] > 0:
            stack.append(asteroids[i])
            i += 1
        elif stack[-1] < 0 and asteroids[i] < 0:
            stack.append(asteroids[i])
            i += 1
        elif stack[-1] > 0 and asteroids[i] < 0:
            while stack and abs(asteroids[i]) >= abs(stack[-1]) and stack[-1] > 0:
                stack.pop()
            i += 1
        else:
            i += 1
    return stack


print(asteroidCollision([-1,3,2,-3,4]))
