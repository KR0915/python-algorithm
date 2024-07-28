N=int(input())
l=[]
for _ in range(N):
    S=input()
    l.append(S)
    
for i in range(N-2):
    if l[i]=='sweet' and l[i+1]=='sweet':
        print('No')
        break
else:
    print('Yes')
        