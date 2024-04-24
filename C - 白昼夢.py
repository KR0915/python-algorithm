S=input()

T=["dreameraser","dreamerase","dream","dreamer","erase","eraser"]

for i in T:
    S=S.replace(i,"")
    
if len(S)!=0:
    print('NO')
else:
    print('YES')