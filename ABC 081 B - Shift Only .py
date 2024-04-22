a=int(input())
b=list(map(int,input().split()))

counter=0
while True:
    j=True
    for i in range(a):
        if b[i]%2==1:
            j=False
        else:
            b[i]=b[i]//2
    
    if j:
        counter+=1
    else:
        break

print(counter)
        