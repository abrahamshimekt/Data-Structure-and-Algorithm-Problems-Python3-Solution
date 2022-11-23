"""The problem is to find a non duplicate string which is the smallest in lexicographically from the
the set of substrings
how to solve the problem
1. the problem is a type of monotonic stack because the question asking to keep the lexicographical order\
2. first what should to do is to keep track the last occurrence of each character
3. the also we should keep track wether the character is seen or not
4. Then iterate through the string if the the current element is less than the element at the top of the
stack we should pop the element at the top of the stack whenever its its index is less than the last ocurrence
of itself. if the element at the current index is seen we are not going to append it to the top of the
stack 
"""