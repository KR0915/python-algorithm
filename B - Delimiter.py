a=[]
A=[]
while A!=0:
    A=int(input())
    a.append(A)

for i in range(1,len(a)+1):
    print(a[-i])
