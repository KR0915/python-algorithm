N=int(input())
S=input()
flag=True
for i in range(N-2):
    if S[i]+S[i+1]+S[i+2]=='ABC':
        print(i+1)
        flag=False
        break
    
if flag:
    print(-1)