"""
The problem is to check if it is possible to transport passengers
from i position j position and the vehicle has a limited capacity
steps to solve the problem
1.take  the first k number of passengers under the capacity constraint since the vehicle is empty
2. then ask if the current passengers are arrived or not before taking the next passengers: if the
current passengers arrived decrease their number from the current number of passengers then take next passengers and the
capacity constraint else if the passengers are not arrived and taking more passengers not exceeded the
capacity constraint, then take the next passengers else take not them and return False
[[3,2,8],[4,4,8],[10,8,9]]
11
temp = 6
np = 7
i = 3
"""


def carPooling(self, trips, capacity) -> bool:
    numpassengers = trips[0][0]
    temp = float("inf")
    if numpassengers > capacity:
        return False
    i = 1
    while i < len(trips):
        if trips[i - 1][2] <= trips[i][1]:
            numpassengers -= trips[i - 1][0]
            if temp < trips[i - 1][2]:
                numpassengers = 0
            numpassengers += trips[i][0]
            if numpassengers > capacity:
                return False
            i += 1
        elif numpassengers + trips[i][0] <= capacity:
            numpassengers += trips[i][0]
            temp = trips[i][2]
            trips[i][2] = trips[i-1][2]
            i += 1
        else:
            return False
    return True
