N=int(input())
S=input().split()

seen=set()
counter=0
for sock in S:
    if sock in seen:
        counter+=1
        seen.remove(sock)
    else:
        seen.add(sock)
        
    print(seen)
        
print(counter)