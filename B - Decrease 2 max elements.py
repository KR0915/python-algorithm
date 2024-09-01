N = int(input())
A = list(map(int, input().split()))
count = 0

while len([x for x in A if x > 0]) > 1:
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    A = [x for x in A if x > 0]  # 0以下の数を除去
    count += 1

print(count)