N, A, B = map(int, input().split())
def sum(num):
    sum=0
    while num>0:
        sum+=num%10
        num//=10
    return sum

total=0
for i in range(1,N+1):
    s=sum(i)
    if s>=A and s<=B:
        total+=i
print(total)
    
    