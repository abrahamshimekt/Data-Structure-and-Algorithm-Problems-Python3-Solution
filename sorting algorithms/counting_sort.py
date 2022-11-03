"""
{1, 4, 1, 2, 5, 2}
[0,0,0,0,0,0]
[0,1,2,3,4,5]
[0,2,2,0,1,1]
[0,2,4,4,5,6]
[1,1,2,2,4,5]
how to implement counting sort:
1. create a list with size of the max of the nums array plus one that has zero elements
2. Then count the numbers of the occurrences of each element
3. then append the index in their occurrence time.
The counting sort algorithm is a total of O(N) time complexity
"""


def counting_sort(nums):
    freq = [0] * (max(nums) + 1)  # O(N)
    output = []
    for num in nums:  # O(N)
        freq[num] += 1
    for i in range(len(freq)):  # O(N)
        if freq[i] == 0:
            continue
        else:
            j = freq[i]
            while j > 0:
                output.append(i)
                j -= 1
    return output


print(counting_sort([1, 4, 1, 3, 2, 5, 2, 5, 5, 5, 3, 3, 3, 0]))
