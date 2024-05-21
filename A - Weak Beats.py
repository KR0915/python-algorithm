S=input()
for i in range(1,9):
    if S[i*2-1]!='0':
        print('No')
        break
else:
    print('Yes')