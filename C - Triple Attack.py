N=int(input())
H=list(map(int,input().split()))

ans=0
for j in range(N):
    if ans%3==0:
        if H[j]%5==0 or H[j]%5==1 or H[j]%5==2:
            ans+=(H[j]//5)*3+(H[j]%5)*1
        elif H[j]%5==3 or H[j]%5==4:
            ans+=(H[j]//5)*3+3
    elif ans%3==1:
        if H[j]>4:
            H[j]=H[j]-4
            if H[j]%5==0 or H[j]%5==1 or H[j]%5==2:
                ans+=(H[j]//5)*3+(H[j]%5)*1+2
            elif H[j]%5==3 or H[j]%5==4:
                ans+=(H[j]//5)*3+3+2
        elif H[j]==1:
            ans+=1
        elif 2<=H[j]<=4:
            ans+=2
    elif ans%3==2:
        if H[j]>3:
            H[j]=H[j]-3
            if H[j]%5==0 or H[j]%5==1 or H[j]%5==2:
                ans+=(H[j]//5)*3+(H[j]%5)*1+1
            elif H[j]%5==3 or H[j]%5==4:
                ans+=(H[j]//5)*3+3+1
        else:
            ans+=1
            
print(ans)