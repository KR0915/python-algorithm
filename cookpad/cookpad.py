import sys
#指定されたファイルから座標を読み取り、ソートした値を返す
def read_locations(file_path):
    with open(file_path, 'r') as file:
        return sorted([int(line.strip()) for line in file])

#最小距離を保ちつつ、自販機をすべて配置できるかどうかをチェックする
def min_vending(locations, num_vending_machines, min_distance):
    count = 1
    last_position = locations[0]
    
    for location in locations[1:]:
        if location - last_position >= min_distance:
            count += 1
            last_position = location
            if count == num_vending_machines:
                return True
                
    return False
#二分木探索を使用し、最大の最小距離を見つける
def find_max_distance(locations, num_vending):
    left = 1
    right = locations[-1] - locations[0]
    best = 0
    
    while left <= right:
        mid = (left + right) // 2
        if min_vending(locations, num_vending, mid):
            best = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return best

def main():
    if len(sys.argv) != 3:#コマンドラインからファイルパスと自販機の数を取得する
        print('Usage: python cookpad.py <file_path> <num_vending_machines>')
        return
    
    file_path = sys.argv[1]
    num_vending = int(sys.argv[2])
    
    locations = read_locations(file_path)
    max_distance = find_max_distance(locations, num_vending)
    print(max_distance)

if __name__ == '__main__':
    main()
