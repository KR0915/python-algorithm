import math
N=int(input())
A=math.floor(N/1.08)
if A*1.08<N:
    print(":(")
else:
    print(A)
    
print(A*1.08)