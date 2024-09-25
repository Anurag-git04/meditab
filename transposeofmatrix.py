def transpose(A,B):
    N = len(A[0])
    for i in range(N):
           for j in range(N):
                 B[i][j] = A[j][i]
    return B

a=[[1,2,3],
     [4,5,6],
     [7,8,9]]
N= len(a[0])
b=[[0 for x in range(N)]for y in range(N)]
answer = transpose(a,b)

print(answer)