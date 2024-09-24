#数値xと複数の範囲が与えられたときに、xが与えられた範囲のどれかに含まれていたらtrue, そうじゃなければfalseを返す関数をかいてください
#xとして10, 範囲は 1-5 と 8-12 と 20-30 => true
#xとして7, 範囲は 2-6 と 10-50 => false
#10
#1-5,8-12,20-30
# X=input()
# range=list(map(input().split()))
def checker(X,range):
    flag=False
    for i in range:
        print(i)
        if i[0]<X<i[-1]:
            flag=True
            
    if flag:
        print('true')
    else:
        print('false')

print(checker(10,[[1,5],[8,12],[20,30]]))
        