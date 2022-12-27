''''A matrix is called identity if all elements on the diagonal are 1 and zero anywhere else.
'''

A = [[1,0,0],[1,1,0],[0,0,1]]
def is_identity_matrix(A):
    m = len(A)
    n = len(A[0])
    for i in range(m):
        for j in range(n):
            if i != j and A[i][j] != 0:
                return False
            elif i == j and A[i][j] != 1:
                return False
    return True
print(is_identity_matrix(A))