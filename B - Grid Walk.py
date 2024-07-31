H,W=map(int,input().split())
S_i, S_j=map(int,input().split())
grid = [input() for _ in range(H)]
X = input()

S_i -= 1
S_j -= 1

for command in X:
    if command == 'L':
        if S_j > 0 and grid[S_i][S_j - 1] == '.':
            S_j -= 1
    elif command == 'R':
        if S_j < W - 1 and grid[S_i][S_j + 1] == '.':
            S_j += 1
    elif command == 'U':
        if S_i > 0 and grid[S_i - 1][S_j] == '.':
            S_i -= 1
    elif command == 'D':
        if S_i < H - 1 and grid[S_i + 1][S_j] == '.':
            S_i += 1

print(S_i + 1, S_j + 1)
