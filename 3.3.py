def merge_sort(L,R):
    if len(L)>1:
        L=merge_sort(L[:len(L)//2],L[:len(L)//2])
    if len(R)>1:
        R=merge_sort(R[:len(L)//2],R[:len(L)//2])
    M=[]
    while len(L)>0 and len(R)>0:
        if L[0]>R[0]:
            M.append(L.pop(0))
        else:
            M.append(R.pop(0))
    if len(L)>0:
            M.extend(L)
    elif len(R)>0:
            M.extend(R)
    return M