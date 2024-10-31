S=input()
T=input()
N=len(S)
X=[]
while S!=T:
    ns="z"*N
    for i in range(N):
        if S[i]!=T[i]:
            ns=min(ns,S[:i]+T[i]+S[i+1:])#これで辞書順を判定できる
    X.append(ns)
    S=ns

print(len(X))
for x in X:
    print(x)