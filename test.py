# 入力された値（すべてstr型）をリストに格納します
input_values = ["1", "2", "3", "a", "b", "c", "4", "5"]

# int型に変換できる値とそうでない値を格納するためのリストを作成します
convertible_to_int = []
not_convertible_to_int = []

# 値をint型に変換し、変換できるかどうかを確認します
for value in input_values:
    try:
        converted_value = int(value)
        convertible_to_int.append(converted_value)
    except ValueError:
        not_convertible_to_int.append(value)

# 結果を出力します
print("int型に変換できる値:", convertible_to_int)
print("int型に変換できない値:", not_convertible_to_int)


