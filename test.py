from bisect import bisect_left

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N, M = int(data[0]), int(data[1])
    A = list(map(int, data[2:N+2]))
    B = list(map(int, data[N+2:]))
    
    # 美食度と人のインデックスをペアにしてソート
    people = sorted((a, i + 1) for i, a in enumerate(A))
    
    result = []
    for b in B:
        # 二分探索で条件を満たす最初の人を探す
        idx = bisect_left(people, (b, 0))
        if idx < len(people) and people[idx][0] <= b:
            # 寿司を取る人を確定
            result.append(people[idx][1])
            people.pop(idx)  # 人を削除（その人はもう寿司を取れない）
        else:
            # 誰も寿司を取れない場合
            result.append(-1)
    
    sys.stdout.write('\n'.join(map(str, result)) + '\n')

# 実行
solve()