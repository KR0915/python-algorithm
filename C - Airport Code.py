S = input()
T = input().lower()
flag = 0

if T[-1:] == 'x':
    T = T[:-1]

    for i in S:
        if i == T[flag]:
            if flag >= 1:
                print('Yes')
                exit()
            else:
                flag += 1     
else:
    for i in S:
        if i == T[flag]:
            if flag >= 2:
                print('Yes')
                exit()
            else:
                flag += 1
        
print('No')