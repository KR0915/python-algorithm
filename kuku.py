for n in range(1,1+9):
    line='|'
    for m in range(1,1+9):
        value=n*m
        line+=f'{value:3d}|'#
    print(line)