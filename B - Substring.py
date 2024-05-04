S=input()
ans=0
get=[]
for i in range(len(S)+1):
    for j in range(i+1,len(S)+1):
        get.append(S[i:j])


ans=set(get)
print(len(ans))