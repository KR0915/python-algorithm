K,G,M=map(int,input().split())
g=0
m=0
for i in range(K):
    if m==0 and g==0:
        m=M
    elif m==M and g<G:
        m=M-G
        g=G
    elif m>0 and g<G and m-G<=0:
        g=m
        m=0
    elif g==G:
        g=0
print(g,m)