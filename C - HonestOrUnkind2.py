N = int(input())
test = []
for _ in range(N):
    A = int(input())
    person = []
    for _ in range(A):
        X, Y = map(int, input().split())
        person.append((X - 1, Y))
    test.append(person)

max_honest = 0

for bit in range(1 << N):
    is_consistent = True
    for i in range(N):
        if bit & (1 << i):
            for X, Y in test[i]:
                if (bit >> X) & 1 != Y:
                    is_consistent = False
                    break
        if not is_consistent:
            break
    if is_consistent:
        max_honest = max(max_honest, bin(bit).count('1'))

print(max_honest)