N=int(input())
p=[] 
for i in range(N):
    input_list=list(map(int,input().split()))
    p.append(input_list)
    p.sort()
    
print(p)

for i in p:
    print(i[0],i[1])
    print(i)