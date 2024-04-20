a=int(input())
b=list(map(int,input().split()))
j=True
counter=0
for i in b:
    if i%2==1:
        j=False
        break
        
if j:
    for i in range(a):
        b[i]=b[i]//2
        counter+=1
        
print(counter)