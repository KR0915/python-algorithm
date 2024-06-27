Sx,Sy = map(int, input().split())
Tx,Ty = map(int, input().split())
if abs(Sy-Ty)<=1:
    print(0)
elif Sy>Ty:
    print(abs(Sy-Ty))
elif Sy<Ty:
    print(abs(Ty-Sy))

