S=input()
T=input()
S1=S[0]
S2=S[1]
T1=T[0]
T2=T[1]
P=['E','A','B','C','D','E','A']
ansS=0
ansT=0
for i in range(1,6):
    if (P[i]==S1 and P[i+1]==S2) or (P[i]==S1 and P[i-1]==S2):
        ansS=1
    
    if (P[i]==T1 and P[i+1]==T2) or (P[i]==T1 and P[i-1]==T2):
        ansT=1
        
if ansS==ansT:
    print('Yes')
else:
    print('No')
    

