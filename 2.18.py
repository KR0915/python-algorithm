import random 

num=100
x=random.sample(range(num),num)#乱数でnum個の数値をリストxに保存

for k in range(num-1,0,-1):
    for j in range(k):
        if x[j]<x[j+1]:#隣同士(x[j]とx[j+1]の比較)
            x[j],x[j+1]=x[j+1],x[j]#x[j]とx[j+1]の入れ替え