A,B=map(int,input().split())
i=0
if B==1:
    i=0
else:
    while ((A*i)-(i-1))<B:
        i+=1
print(i)