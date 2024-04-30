s=input()

ans=[]
for i in range(len(s)):
    count=0
    for j in range(len(s)):
        if s[i]==s[j]:
            count+=1
    ans.append(count)
ans.sort()
print(ans)

for i in ans:
    

