"""
Approach:
Using two pointer we can keep track of the number of the occurrence of the elements : if the number of the occurrence
of a given ith item is less than or equal to two we don't need to swap the ith  plus one element and the j the
element. but if we have a count greater than two we have to swap the and set the count to zero to the newly
add ith element.
"""
print(bin(2))