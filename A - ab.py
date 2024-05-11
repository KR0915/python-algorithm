N=int(input())
S=input()
flag=False
for i in range(N):
    if S[i:i+2]=='ab' or S[i:i+2]=='ba':
        flag=True
        break
if flag:
    print("Yes")
else:
    print("No")