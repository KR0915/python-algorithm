n=input()
result=[]
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            #n=n[:i]+n[i+1:]
            result.append(i)
            print(n)
            break
            
for j in sorted(result, reverse=True):
    n = n[:j] + n[j + 1:]
print(n)
print(result)
                
