N,Q=map(int,input().split())
S=input()
L=[]
ans=S.count('ABC')
S=list(S)
for _ in range(Q):
    X,C=map(str,input().split())
    X=int(X)-1
    tmp=0
    for i in range(max(0,X-2),min(len(S)-1,X+1)):
        if S[i:i+3]==['A','B','C']:
            ans-=1
            
    S[X]=C
    for i in range(max(0,X-2),min(len(S)-1,X+1)):
        if S[i:i+3]==['A','B','C']:
            ans+=1
            
    print(ans)
    

