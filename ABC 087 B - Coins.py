a=int(input())
b=int(input())
c=int(input())
X=int(input())
counter=0
for c500 in range(a+1):
    for c100 in range(b+1):
        for c50 in range(c+1):
            total=500*c500+100*c100+50*c50
            if total==X:
                counter+=1
print(counter)