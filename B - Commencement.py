N=input()
count=0
for i in range(len(N)):
    for j in range(len(N)):
        if N[i]==N[j+1]:
            count+=1
            if count==0 or count==2:
                