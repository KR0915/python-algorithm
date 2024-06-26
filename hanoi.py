#ハノイの塔を再帰で解く関数
def hanoi(n,source,destination,temp):
    if n==1:
        #円盤一枚なら対象を目的地に移動
        move_disk(source,destination)
    if n>=2:
        #円盤二枚以上の場合の処理
        #nより上の円盤を再帰によって待避用の杭に移動
        hanoi(n-1,source,temp,destination)
        #n(一番下の円盤)を目的地に移動
        move_disk(source,destination)
        #先ほど待機用の杭に移動した円盤を再帰によって目的地に移動
        hanoi(n-1,temp,destination,source)
        
#円盤の移動を表示する関数
def move_disk(source,destination):
    print(f'{source}→{destination}')
    
if __name__=="__main__":
    #円盤が3枚の時の手順を表示する
    hanoi(3,'A','C','B')