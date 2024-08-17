N=int(input())
main_count=0
for j in range(1,N+1):
    count=0
    if j%2!=0:
        for i in range(1,N+1):
            if j%i==0:
                count+=1
        if count==8:
            main_count+=1
            
print(main_count)   
            
        
