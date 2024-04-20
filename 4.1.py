def quick_sort(x):
    if len(x)>1:
        pivot=x.pop(-1)
        left=[]
        right=[]
        mid=[pivot]
        for data in x:
            if data>pivot:
                left.append(data)
            elif data<pivot:
                right.append(data)
            else:
                mid.append(data)
        x=quick_sort(left)+mid+quick_sort(right)
    return x