s=input("Введите слово: ")
l = len(s)
if l %2 !=0:
    l+=1
l//=2
print(s[l:]+s[:l])
