'''The dot product of to vector is an element wise operation meaning we can multiply componnets with
the same coordinate
let use A = (ax,ay,az) and B = (bx,by,bz)
A.B = ax*bx + ay*by + az*bz
A.B = ||A||*||B||*cose(X) where x is the angle between A and B, angle show relationship in machine learning

'''
def dot_product(A,B):
    # the two vectors should have the same number of elements
    n = len(A)
    m = len(B)
    product = 0
    if n == m:
        for index in range(n):
            product += A[index]*B[index]
    return product
print(dot_product([3,4,5],[1,3,2]))
