# M1 = int(input("Enter the first matrix"))

A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
B = [[2,4,6,9],
     [1,2,4,6],
     [8,6,4,2]]

result = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]

for i in range (len(A)):
    for j in range (len(B[0])):
        for k in range (len(B)):
            result[i][j] += A[i][k] * B[k][j]
#print(result) # this will print in a straight line not in a matrix
for i in result:
    print (i)
