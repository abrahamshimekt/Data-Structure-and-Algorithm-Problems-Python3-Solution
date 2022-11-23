""""
how the algorithm works like the following ways:
1. divide the array as sorted and unsorted
2. consider the first val of array as sorted and in the right position
3. each time select an item to be sorted or move to the left
4. start from the next val of the array and compare ith element of array with its previous element
 until the ith element found the right position. move the ith element
 to the left until i >  0 and the ith element is less than its previous one and swap the ith element and ith -1 element
[0, 1,3,6,4, 5, 7]
i = 2
valtosort =3

"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        val_to_sort = arr[i]
        while i > 0 and arr[i - 1] > val_to_sort:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr


print(insertion_sort([5,2,2,99, 3, 1, 7]))
