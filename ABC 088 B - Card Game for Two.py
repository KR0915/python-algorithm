N=int(input())
elements=list(map(int,input().split()))
elements.sort(reverse=True)

Alice=0
Bob=0

for i in range(N):
    if i%2==0:
        Alice+=elements[i]
    else:
        Bob+=elements[i]
        
result=Alice-Bob
print(result)
        

    
