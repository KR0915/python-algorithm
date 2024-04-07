#素数かどうかを判定するプログラム
def is_prime(n):
    if n<2:return False
    
    for i in range(2,n):
        if n%i==0:return False
    return True

#値をカンマで区切り10個ずつ改行して返す
def get_prime_game(max_value):
    res=''
    for n in range(1,max_value+1):
        if is_prime(n):
            v='p'
        else:
            v=n
        res+='{:>4}'.format(v)
        
        if(n-1)%10==9:
            res+='\n'
        else:
            res+=','
    return res

if __name__=='__main__':
    print(get_prime_game(200))