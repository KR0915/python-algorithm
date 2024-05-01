N=int(input())
a=0
b=0
for i in range(N):
    A,B=map(int,input().split())
    a+=A
    b+=B
if a==b:
    print('Draw')
elif a>b:
    print('Takahashi')
else:
    print('Aoki')
