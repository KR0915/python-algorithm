N,A,B=map(int,input().split())
S=list(map(str,input().split()))
a_count=0
b_count=0
for i in range(len(S)):
    if S[i]!='c':
        if S[i]=='a':
            if a_count+b_count<=A+B:
                print('Yes')
                a_count+=1
        elif S[i]=='b':
            if a_count+b_count<=A+B and b_count<=B:
                print('Yes')
                b_count+=1
    else:
        print('No')