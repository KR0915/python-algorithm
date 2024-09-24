import sys

def main(lines):
    N, A, M, K = map(int, lines[0].split())

    ans = 0

    if N * K != M:
        if N * K > M:  # 平均点より最大点が低い場合
            while M > K * N:
                M += A
                ans += 1
                if M > K * N:  # 必要に応じて条件を追加してください
                    break
        elif N * K < M:  # 平均点より最大点が高い場合
            while N * K < M:
                K += 1
                ans += 1

    print(ans)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
