N=input()
d=len(N)
ans=100

#num=(000...0)～(111...1)
#0,1の組み合わせをすべて試す。
for num in range(1<<d):
    #桁を消してくれる数字
    N_tmp=""
    #消した個数
    ans_tmp=0
    #shift=0~(d-1)
    for shift in range(d):
        #1&(numをshift個右シフト)=1ならば
        if 1 & num>>shift==1:
            #その桁を使う
            N_tmp=N_tmp+N[shift]
        #1&(numをshift個右シフト)=0ならば
        else:
            #桁を消した個数をカウント
            ans_tmp+=1
            
    #N_tmpが空文字列ならば
    #num=(000...0)の場合
    if N_tmp=="":
        #次のnumへ
        continue
    
    #整数にして３で割り切れる場合
    if int(N_tmp)%3==0:
        #ansによりans_tmpが小さければ更新
        ans=min(ans,ans_tmp)
        
#答えが更新されていれば
if ans==100:
    print(-1)
else:
    print(ans)