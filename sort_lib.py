#sortメソッドを使う
a_list=[5,2,4,1,3]
a_list.sort()
print(a_list)

#soreted関数を使う
b_list=[5,2,4,1,3]
b_list2=sorted(b_list)
print(b_list2)

#降順にソートする場合
c_list=[5,2,4,1,3]
c_list.sort(reverse=True)
print(c_list)

d_list=[5,2,4,1,3]
d_list2=sorted(d_list,reverse=True)
print(d_list2)