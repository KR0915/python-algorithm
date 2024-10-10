N,Q=map(int,input().split())
S=input()
L=[]
ans=S.count('ABC')
for _ in range(Q):
    M=list(input().split())
    L.append(M)
    
for i in L:
    # S=S[:int(i[0]-1)]+i[1]+S[int(i[0]):]
    if (S[int(i[0])-1]=='A' and (S[int(i[0])]=='B') and (S[int(i[0]+1)]=='C')) or (S[int(i[0])-1]=='B' and (S[int(i[0])]=='C') and (S[int(i[0]-2)]=='A')) or (S[int(i[0])-1]=='C' and (S[int(i[0]-2)]=='B') and (S[int(i[0]-3)]=='A')):
        if i[1]!=S[int(i[0])-1]:
            ans-=1
        else:
            pass
    else:
        if i[1]=='A' and S[int(i[0])-1]=='B' and S[int(i[0])]=='C':
            ans+=1
        elif i[1]=='B' and S[int(i[0])-1]=='C' and S[int(i[0])]=='A':
            ans+=1
        elif i[1]=='C' and S[int(i[0])-1]=='A' and S[int(i[0])]=='B':
            ans+=1
            
    print(ans)

