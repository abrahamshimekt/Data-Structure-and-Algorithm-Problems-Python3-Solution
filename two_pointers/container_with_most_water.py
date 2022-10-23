"""
 The problem is to find the maximum volume of water
 height = [1,8,6,2,5,4,8,3,7]

"""


def mostWater(heights):
    i, j = 0, len(heights) - 1
    most_water = 0
    while i <= j:
        if heights[i] <= heights[j]:
            most_water = max(most_water, heights[i] * (j - i))
            i += 1
        else:
            most_water = max(most_water, heights[j] * (j - i))
            j -= 1
    return most_water


print(mostWater([1, 8, 6, 2, 5, 4, 8, 3, 7]))
