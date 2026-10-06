words=[]
res=[]
while 1:
    s=input(">")
    if s !="":
        if s not in words:
            words.append(s)
    else:
        break
#print(words)
for word in words:
    if word not in res:
        res.append(word)
print(res)
