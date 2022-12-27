''''If B is a transpose of matrix A mxn then B is nxm '''
A = [[3,4],[0,1]]
def find_transpose(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(A[j][i])
        B.append(row)
    return B
print(find_transpose(A))
