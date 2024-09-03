N=int(input())
S=list(map(int,input().split()))
Q=int(input())
T=list(map(int,input().split()))
S.sort()
count=0
for i in T:
    left, right = 0, N - 1  # ループの中で初期化
    while left<=right:
        mid=(left+right)//2
        if i==S[mid]:
            count+=1
            break
        elif S[mid]>i:
            right=mid-1
        else:
            left=mid+1
            

print(count)