def create_carpet(N):
    if N == 0:
        return ["#"]
    
    # Previous level carpet
    smaller_carpet = create_carpet(N - 1)
    size = len(smaller_carpet)
    new_size = size * 3
    new_carpet = []
    
    for i in range(new_size):
        if size <= i < 2 * size:
            # Middle block, center should be white
            new_carpet.append(smaller_carpet[i % size] + '.' * size + smaller_carpet[i % size])
        else:
            # Top and bottom blocks
            new_carpet.append(smaller_carpet[i % size] * 3)
    
    return new_carpet

def print_carpet(carpet):
    for row in carpet:
        print(row)

# 入力を受け取る
N = int(input())

# レベルNのカーペットを生成
carpet = create_carpet(N)

# カーペットを出力
print_carpet(carpet)