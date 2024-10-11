N,Q=map(int,input().split())
S=input()
x=[]
c=[]
for _ in range(Q):
    X,C=input().split()
    X=int(X)
    x.append(X)
    c.append(C)
    
for i in range(Q):
    S=S[:x[i]-1]+c[i]+S[x[i]:]
    print(S.count('ABC'))