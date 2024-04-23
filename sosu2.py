for i in range(1,10001):
    ans=True
    for n in range(2,i):
        if i%n==0:
            break
    else:
        print(i)    
