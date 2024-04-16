def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total

# テスト用のリスト
my_list = [1, 2, 3, 4, 5]

# 関数を呼び出してリストの合計を取得する
result = sum_list(my_list)
print("リストの合計:", result)