W,B=map(int,input().split())
p="wbwbwwbwbwbw"
s=p*(W+B)
ans=False
for i in range(len(p)):
    ans=s[i:i+W+B]