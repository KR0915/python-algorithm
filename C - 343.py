N=int(input())
for i in range(10**6,0,-1):
    result=i**3
    if result<=N and str(result)==str(result)[::-1]:
        print(i**3)
        break
        
    