import random

num=100
x=random.sample(range(num),num)

for k in range(num-1):
    for j in range(k+1,num):
        if x[k]<x[j]:
            x[k],x[j]=x[j],x[k] #x[j]とx[k]の入れ替え
            
print(x)