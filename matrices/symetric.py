'''If a matrix is said to symetric matrix if its transpose is equal to the matrix itself | A = A^T
. A matrix should be a sqaure matrix to be symmetric'''
A = [[3,4],[4,3]]
def is_symmetric(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(A[j][i])
        B.append(row)
    for k in range(m):
        for l in range(n):
            if A[k][l] != B[k][l]:
                return False
    return True
print(is_symmetric(A))

