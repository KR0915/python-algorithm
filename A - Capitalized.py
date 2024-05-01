S=input()
flag=True
if S[0].isupper():
    for i in range(1,len(S)):
        if S[i].isupper():
            print('No')
            flag=False
            break
else:
    print('No')
    flag=False
    
if flag:
    print('Yes')