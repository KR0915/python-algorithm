S=input()
T=input()
t=T.lower()
flag1=False
flag2=False
flag3=False
if t[-1]=='x':
    for i in range(len(S)):
        if t[0]==S[i]:
            flag1=True
        elif t[1]==S[i]:
            flag2=True
    else:
        if flag1 and flag2:
            print('Yes')
        else:
            print('No')
elif t[-1]!='x':
    for i in range(len(S)):
        if t[0]==S[i]:
            flag1=True
        elif t[1]==S[i]:
            flag2=True
        elif t[2]==S[i]:
            flag3=True
    else:
        if flag1 and flag2 and flag3:
            print('Yes')
        else:
            print('No')