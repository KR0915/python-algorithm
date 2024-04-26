S=input()
flag1=False
flag2=False
flag3=False
if S[0]=="<":
    flag1=True
    for i in range(1,len(S)-1):
        if S[i]!="=":
            break
        else:
            flag2=True
    if S[-1]==">":
        flag3=True
        
if flag1 and flag2 and flag3:
    print("YES")
else:
    print("NO")