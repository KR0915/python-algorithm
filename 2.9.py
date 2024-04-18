import random
import time

num=int(1e4)
seed=1
print('The number of data:',num)

print('Selection sort')
random.seed(seed)

x=random.sample(range(num),num)
start=time.perf_counter()

for z in range(num):
    for y in range(z+1,num-1):
        if x[z]<x[y]:
            x[z],x[y]=x[y],x[z]
            
elapsed_time=time.perf_counter()-start
print(elapsed_time,'sec')
print('MAX:',x[0],'MID:',x[int(num/2)],'MIN:',x[num-1])

print('Bubble sort')
random.seed(seed)
x=random.sample(range(num),num)
start=time.perf_counter()
for k in range(num-1,0,-1):
    for j in range(k):
        if x[j]<x[j+1]:#
            x[j],x[j+1]=x[j+1],x[j]#
            
elapsed_time=time.perf_counter()-start
print(elapsed_time,'sec')
print('MAX:',x[0],'MID:',x[int(num/2)],'MIN:',x[num-1])