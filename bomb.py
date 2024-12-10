import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))
    n,m,k = map(int, lines[0].split())
    matrix=[]
    for i in range(1,n+1):
        matrix.append(lines[i])

    rows_to_bomb = set()
    cols_to_bomb = set()
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'B':
                rows_to_bomb.add(i)
                cols_to_bomb.add(j)

    if len(rows_to_bomb) == n or len(cols_to_bomb) == m:
        print(0)
        return

    remaining_values = []
    for i in range(n):
        if i in rows_to_bomb:
            continue
        for j in range(m):
            if j in cols_to_bomb:
                continue
            remaining_values.append(int(matrix[i][j]))

    bombed_values = []
    for i in range(n):
        if i in rows_to_bomb:
            for j in range(m):
                if matrix[i][j] != 'B':
                    bombed_values.append(int(matrix[i][j]))
        else:
            for j in cols_to_bomb:
                if matrix[i][j] != 'B':
                    bombed_values.append(int(matrix[i][j]))
    
    if len(remaining_values)>k:
        k=len(remaining_values)

    remaining_values.sort()
    # print(remaining_values)
    min_values = remaining_values[:k]
    # print(min_values)

    bombed_values.sort(reverse=True)
    print(bombed_values)
    max_values = bombed_values[:k]
    print(max_values)
    total_sum = sum(remaining_values) - sum(min_values) + sum(max_values)
    
    if n==1 and m==1 and  matrix[0][0]!='B':
        print(int(matrix[0][0]))
    # elif len(remaining_values)==1 and k>=1:
    #     print(max(remaining_values,max(bombed_values)))
    else:
        print(total_sum)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
