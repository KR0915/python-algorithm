count=0
for c1 in range(0,522):
    for c5 in range(0,106):
        for c10 in range(0,53):
            for c50 in range(0,11):
                for c100 in range(0,6):
                    for c500 in range(0,2):
                        total=c500*500+c100*100+c50*50+c10*10+c1
                        if total==521:
                            count+=1
                            
print(count)