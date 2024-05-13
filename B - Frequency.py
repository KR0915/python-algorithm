S=input()
abc=list("abcdefghijklmnopqrstuvxwz")
ans=[]
for i in range(len(abc)):
    ans.append(S.count(abc[i]))
    
m=max(ans)
    
for k in range(len(ans)):
    if ans[k]==m:
        print(abc[k])
        break
