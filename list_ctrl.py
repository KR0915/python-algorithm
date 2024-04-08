#リストの初期化
a_list=[0,1,2]

#リストに要素を追加
a_list.append(3)
a_list.append(4)

#リスト全体を表示
print('(*3)全体=',a_list)

#リストの新居の値を参照
print('(*4)a_list[3]=',a_list[3])

#リストから要素を削除
del a_list[2]
print('(*5)2を削除',a_list)

#すべての要素を削除
a_list.clear()
print('(*6)clear後の要素数=',len(a_list))