S = input().strip()
T = input().strip()
X = []

S_list = list(S)

for i in range(len(S)):
    if S_list[i] != T[i]:
        S_list[i] = T[i]
        X.append(''.join(S_list))

print(len(X))
if len(X) != 0:
    for x in X:
        print(x)