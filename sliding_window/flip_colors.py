"""The problem is to find the minimum number of white flips inorder to get k number of blacks
How to solve
1. take the first k strings from the array by counting the number of whites. then each time take the minimum
number of whites to flip
2. if the element to be removed is white decrees the count and if the element to added to white increase the
count by one. else just move.
blocks = "WBWBBBW", k = 2
w = 1
fl = 0
j = 5
"""


def minimumRecolors(blocks, k):
    whites = 0
    flips = float("inf")
    for i in range(k):
        if blocks[i] == "W":
            whites += 1
    j = 1
    flips = min(flips, whites)
    while j + k <= len(blocks):
        if blocks[j - 1] == "W":
            whites -= 1
        if blocks[j + k - 1] == "W":
            whites += 1
        flips = min(flips, whites)
        j += 1
    return flips
print(minimumRecolors("WBWBBBW",2))

