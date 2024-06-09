S=input()
c1=0
c2=0
for i in range(len(S)):
    if S[i].isupper():
        c1+=1
    else:
        c2+=1

if c1>c2:
    S=S.upper()
else:
    S=S.lower()
    
print(S)