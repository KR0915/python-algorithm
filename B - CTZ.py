N=int(input())
N=bin(N)[2:]
c=0
for i in range(1,len(N)):
    if int(N[-i])==0:
        c+=1
    else:
        break
print(c)