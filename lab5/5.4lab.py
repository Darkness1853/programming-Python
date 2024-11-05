A=[
    [1,2,3,4],
    [5,6,1,1],
    [2,5,1,0],
    [4,3,2,1]
]
max=A[0][0]
for i in range(len(A)):
    for j in range(len(A[i])):
        if A[i][j]>=max:
            max=A[i][j]
            max_i=i
            max_j=j
print("Максимальный элемент в массиве",max)
print("Расположение максимального элемента",max_i+1,max_j+1)