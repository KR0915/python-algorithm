S=input()
ans=0
for i in range(len(S)):
    if S[i]=='.':
        ans=i+1
        
print(S[ans:])