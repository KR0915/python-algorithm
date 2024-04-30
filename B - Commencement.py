s=input()
result={}
for i in s:
    for i in result:
        result[i]+=1
    else:
        result[i]=1
d=list(result.values())

for j in d:
    if not (d.count(j)in(0,2)):
        print('No')
        break
else:
    print('Yes')
