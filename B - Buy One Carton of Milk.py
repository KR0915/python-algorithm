import math
N,S,M,L=map(int,input().split())
ans=100*3*10**4
for e6 in range(0,math.ceil(N//6)+2):
    for e8 in range(0,math.ceil(N//8)+2):
        for e12 in range(0,math.ceil(N//12)+2):
            if ans>S*e6+M*e8+L*e12 and N<=6*e6+8*e8+12*e12:
                ans=S*e6+M*e8+L*e12
print(ans)