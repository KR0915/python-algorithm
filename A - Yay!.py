S=input()
s=sorted(S)
if s[0]!=s[1]:
    for i in range(len(S)):
        if S[i]==s[0]:
            print(i+1)
            break
elif s[-1]!=s[-2]:
    for i in range(len(S)):
        if S[i]==s[-1]:
            print(i+1)
            break
