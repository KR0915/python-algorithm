#入力値の受け取り
N,W=map(int,input().split())

#(1)表を作る
dp=[[0]*(W+1) for i in range(N+1)]

#(3)表の小さいほうから答えにたどり着くまで埋める
#i=1～Nまで
for i in range(1,N+1):
    #i番目の品物の重さと価値
    wi,vi=map(int,input().split())
    #w=0～Wまで
    for w in range(W+1):
        #w-wiがマイナスなら
        if w-wi<0:
            #i番目の品物を入れない
            dp[i][w]=dp[i-1][w]
        #0<=w-wiなら
        else:
            #i番目の品物を入れない
            #i番目の品物を入れる
            #どちらか大きい方
            dp[i][w]=max(dp[i-1][w],dp[i-1][w-wi]+vi)
#(4)答えを出力する     
print(dp[N][W])