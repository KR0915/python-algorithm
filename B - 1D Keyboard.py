S="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SX=input()
counter=0
ans=[]
result=0
for i in range(26):
    for j in range(26):
        if S[i]==SX[j]:
            ans.append(j+1)
            
for i in range(len(ans)):
    if i==0:
        result+=0
    else:
        result+=abs(ans[i]-ans[i-1])  
        
print(result)  