A = [[3,4,4],[3,4,4],[2,6,5]]
B = [[4,6,888],[6,6,6],[2,3,5]]
# matrix is a 2d array of 1d vectors
# let us check first the number of rows and columns of A and B is equal
def matrix_sum(A,B):
    m = len(A)
    n = len(A[0])
    p = len(B)
    q = len(B[0])
    if m==p and n==q:
        C = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(A[i][j] + B[i][j])
            C.append(row)
        return C
    return 'cannot add matrices of different dimension'
print(matrix_sum(A,B))


