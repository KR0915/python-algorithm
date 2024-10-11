N=input()
d=len(N)
N=sorted(N,reverse=True)
ans=0
for num in range(1<<d):
    n=[]
    m=[]
    for shift in range(d):
        if 1 & num>>shift==1:
            n.append(N[shift])
        else:
            m.append(N[shift])
            
    if n==[] or m==[]:
        continue
    
    ans=max(ans,int("".join(n))*int("".join(m)))
    
    
print(ans)