
x=[]
y=[]
for _ in range(3):
    A,B=map(int,input().split())
    x.append(A)
    y.append(B)
    
AB=((x[1]-x[0])**2+(y[1]-y[0])**2)
BC=((x[2]-x[1])**2+(y[2]-y[1])**2) 
CA=((x[0]-x[2])**2+(y[0]-y[2])**2)

if AB+BC==CA or BC+CA==AB or CA+AB==BC:
    print("Yes")
else:
    print("No")