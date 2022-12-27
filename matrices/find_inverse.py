"""
if B is the inverse of matrix A | then AB = I= BA
"""
"""2 by 2 matrix inverse"""
A = [[3,0],[3,4]]
def find_inverse(A):
    m = len(A)
    n = len(A[0])
    determinant = A[0][0]*A[1][1] -(A[0][1]*A[1][0])
    A[0][1] = -1*A[0][1]
    A[1][0] = -1*A[1][0]
    for i in range(m):
        for j in range(n):
            A[i][j] = (1/determinant)*A[i][j]
    return A
print(find_inverse(A))


