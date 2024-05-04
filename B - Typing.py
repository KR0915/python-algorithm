S=input()
T=input()
result=[]
i=0
for j in range(len(T)):
    if S[i]==T[j]:
        result.append(j+1)
        i+=1
            

r=list(set(result))
r.sort()
print(*r)