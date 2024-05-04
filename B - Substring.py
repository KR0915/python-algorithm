S=input()
ans=0
for i in range(len(S)):
    get=set()
    for j in range(len(S)-i):
        get.add(S[i:j])
    ans+=len(get)
print(ans)