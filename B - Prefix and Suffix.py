N,M=map(int,input().split())
S=input()
T=input()

if S[:N]==T[:N] and S[M:]==T[M:]:
    print(0)
elif S[N:]==T[N:]:
    print(2)
elif S[:N]==T[:N]:
    print(1)
else:
    print(3)