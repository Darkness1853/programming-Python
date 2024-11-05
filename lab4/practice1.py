temp=[1,2,3,4,"asd","cvcv",6.7]
print(temp[4])
n=input("Введите количество задач: ")
while isinstance(n,int)!=1 and int(n)>=0:
    n = input("Ошибка! Введите количество задач: ")
n=int(n)
count=0
for i in range(n):
    voices=0
    s = input(">").split()

    for j in s:
        if j !="1" and j !="0":
            print("Error!")
            exit()
        else:
            voices += int(j)
        if voices >=2:
            count+=1
print("Всего можно решить задач:",count)

s=[1,2,"345345"]

