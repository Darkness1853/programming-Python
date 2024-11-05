# A =[ [1,2,3],[4,5,6]]
# print(len(A))
# print(len(A[0]))
# print(A[-1])
# for i in range(2):
#     for j in range(3):
#         print(A[i][j], end =" ")
#     print()
n=int(input("Введите количество строк: "))
m=int(input("Введите количество столбцов: "))

A= [0]*n
for i in range(n):
    A[i]=[0]*m
print(A)