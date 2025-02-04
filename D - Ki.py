#受け取り
N,Q=map(int,input().split())
#つながっている頂点のリストを作る
#1と2,3,4がつながっているならconnect[1]=[2,3,4]
connect=[[]for _ in range(N+1)]

#受け取り
for _ in range(N-1):
    a,b=map(int,input().split())
    #aからb,bからaがつながっている
    connect[a].append(b)
    connect[b].append(a)
    
#各頂点のカウンタを用意
counter=[0]*(N+1)

#受け取り
for _ in range(Q):
    p,x=map(int,input().split())
    #pのcounterにxを足す
    counter[p]+=x

#que=筒を用意する
from collections import deque
que=deque()

#スタート地点=1を入れる
que.append(1)

#訪問済みならチェックを作る
#Falseなら未訪問、Trueなら訪問済み
visited=[False]*(N+1)
#1は訪問済み
visited[1]=True

#que=筒が空になるまで
while len(que)>0:
    #筒の左から取り出してnowに格納
    now=que.popleft()
    #nowのカウンタの値をnow_numberに格納
    now_number=counter[now]
    #nowからつながっている頂点を順番に回る=to
    for to in connect[now]:
        #もしまだ訪問済みでなければ
        if visited[to]==False:
            #counterにnowのカウンタの値を足す
            counter[to]+=now_number
            #訪問済みにチェックを付ける
            visited[to]=True
            #筒に入れる
            que.append(to)
            
# 0以外のcounterを出力
print(*counter[1:])