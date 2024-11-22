S=input()
N=len(S)
counter=0
ans=[]
for i in range(1,N):
    if S[i]=='-':
        counter+=1
    else:
        ans.append(str(counter))
        counter=0
        
print(" ".join(ans))