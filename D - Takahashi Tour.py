#再帰関数の最初に必ず記述すること
import sys
sys.setrecursionlimit(10**9+9999)

N=int(input())
#道の情報の受け取り

connect=[[] for _ in range(N+1)]
#道の格納リスト

for _ in range(N-1):
    A,B=map(int,input().split())
    connect[A].append(B)
    connect[B].append(A)
#connect[2]=[1,4]ならば2と1,4がつながっている
# print(connect)
#小さい順に回るからソート
for i in range(N):
    connect[i].sort()
# print(connect)
    
#答え格納用リスト
ans=[]

#DFS(今いる町、前いた町)
def DFS(now,pre):
    #今いる町を答えに入れる
    ans.append(now)
    #to=今いる町から行ける町
    for to in connect[now]:
        #もしtoが前いた町と違うなら
        if to!=pre:
            #さらに奥に探索する
            DFS(to,now)
            #戻ってきたらこたえへ格納
            ans.append(now)

#最初の町=1,前いた町=-1(前にいた町がないから便宜上)
DFS(1,-1)

print(*ans)