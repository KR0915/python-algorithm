def sosu(s):
    if s<2:
        return False
    for i in range(2,s):
        if s%i==0:
            return False
        
s=int(input())
if sosu(s)==False:
    print("NO")
else:
    print("YES")