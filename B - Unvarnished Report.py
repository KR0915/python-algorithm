S = input()
T = input()

if len(S) == len(T):
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i + 1)
            break
    else:
        print(0)
else:
    min_len = min(len(S), len(T))
    for i in range(min_len):
        if S[i] != T[i]:
            print(i + 1)
            break
    else:
        print(min_len + 1)