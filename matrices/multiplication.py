# the multiplication of two matrices in mathematics goes like this
''''
Two matrices should have equal number of rows and columns .
lets take A with mxn and B with pxq. if C = AB whenever n == p and C will be mxq
'''
A = [[0.25, 0.0], [-0.25, 0.3333333333333333]]
B = [[3,0],[3,4]]
'''
For square matrices A and B  AB takes O(N^3) time complexity. The reason many because of the nature of matrices
multiplication of a matrix is performed row by column.so for a single row we will iterate N^2. thus for n rows we will iterate N*N^2 = N^3
'''
def multiply_matrices(A,B):
    m = len(A)
    n = len(A[0])
    p = len(B)
    q = len(B[0])
    if n==p:
        C = []
        for i in range(m):
            row = []
            for j in range(q):
                product = 0
                for k in range(p):
                    product += A[i][k]*B[k][j]
                row.append(product)
            C.append(row)
        return C
    return 'multiplication is not possible'
print(multiply_matrices(A,B))

