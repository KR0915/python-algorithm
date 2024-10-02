N=int(input())
ans=[]
while N>0:
    power=0
    while 3**(power+1)<=N:
        power+=1
    ans.append(power)
    N-=3**power
    
A=len(ans)
print(A)
print(' '.join(map(str,ans)))