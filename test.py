N=int(input())
A=list(map(int,input().split()))
ans=0
j=0
a=1
for i in range(a,N):
    ans+=(A[i]+A[j])%10**8
    print(i)
    if i==N-1:
        a+=1
        j+=1
    print(ans)
print(ans)
    



