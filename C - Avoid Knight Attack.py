def is_valid(x, y, N):
    return 1 <= x <= N and 1 <= y <= N

N, M = map(int, input().split())
occupied = set()
for _ in range(M):
    a, b = map(int, input().split())
    occupied.add((a, b))

knight_moves = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

attacked = set()
for a, b in occupied:
    for dx, dy in knight_moves:
        x, y = a + dx, b + dy
        if is_valid(x, y, N):
            attacked.add((x, y))
            
attacked -= occupied

safe_count = N**2-len(attacked)-M

print(safe_count)