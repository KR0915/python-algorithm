N,M,K=map(int,input().split())
C,A,R=[],[],[]
for i in range(M):
    input_list=list(input().split())
    C.append(int(input_list[0]))
    A.append(list(map(int,input_list[1:-1])))
    R.append(input_list[-1])

ans=0
for mask in range(1<<N):
    ok=True
    for i in range(M):#テストをループ
        cnt=0
        for a in A[i]:
            cnt+=(mask>>(a-1)) & 1
        ok&=(cnt>=K)==(R[i]=="o")
    ans+=ok
        
print(ans)
    
    