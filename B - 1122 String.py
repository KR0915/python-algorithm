S=input()
N=len(S)
if N % 2 != 0:
    print('No')
    exit()
else:
    for i in range(0, N, 2):
        if S[i] != S[i + 1]:
            print('No')
            exit()
            
    from collections import Counter
    count = Counter(S)
    for value in count.values():
        if value != 2:
            print('No')
            exit()
            
    print('Yes')