for c1 in range(0,12+1):
    for c5 in range(0,9+1):
        for c10 in range(0,30+1):
            total=(c10*10)+(c5*5)+c1
            if total==325:
                print(f'10円*{c10}+5円*{c5}+1円*{c1}')
                