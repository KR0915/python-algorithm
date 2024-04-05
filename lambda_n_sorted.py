in_data=['aa:50','bb:20','cc:80']

print('普通にソート')
print(sorted(in_data))

print('4文字目以降を整数に変換してソート')
print(sorted(in_data,key=lambda s:int(s[3:])))

