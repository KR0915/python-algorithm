for i in range(1,100):
    ans=True
    for n in range(2,i):
        if i%n==0:
            ans=False
    if ans:
        print(i)
