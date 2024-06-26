#再帰的にフィボナッチ数を計算する関数
def fib(n):
    if n<=1:
        return 1
    return fib(n-2)+fib(n-1)

#n個のフィボナッチ数列を求める関数
def fib_list(n):
    return [fib(i) for i in range(0,n)]

#テスト
def test_fib_list2():
    assert fib_list(3)==[1,1,2]
    assert fib_list(8)==[1,1,2,3,5,8,13,21]
    
if __name__=='__main__':
    #フィボナッチ数列を11個表示する
    print(fib_list(38))