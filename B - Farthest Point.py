import math
N=int(input())
result=0
x=[]
y=[]
for i in range(N):
    X,Y=map(int,input().split())
    x.append(X)
    y.append(Y)
for i in range(N):
    ans=0
    for j in range(N):
        if i==j:
            continue
        if ans<math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2) or (math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)==ans and j<result):
            ans=math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            result=j
    print(result+1)