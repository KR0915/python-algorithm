#変数の初期化
AMOUNT=278#用意したい金額
num_pattern=0#組合わせ数の調査用
min_coin=9999#最小コイン枚数（適当に大きな数を指定）
min_comb=[0,0,0]#最小コイン枚数の組み合わせ
max_coin=0#最大コイン枚数
max_comb=[0,0,0]#最大コインの組み合わせ

#総当たりで調べる
for c1 in range(0,19):
    for c5 in range(0,21):
        for c10 in range(0,31):
            #合計金額を決める
            total=c10*10+c5*5+c1
            #用意した金額と異なれば次へ
            if total!=AMOUNT:
                continue
            #組み合わせ数
            num_pattern+=1
            #コインの枚数は
            num_coin=c10+c5+c1
            #一番少ない硬貨か調べる
            if min_coin>num_coin:
                min_coin=num_coin
                min_comb=[c10,c5,c1]
            #一番多い硬貨か調べる
            if max_coin<num_coin:
                max_coin=num_coin
                max_comb=[c10,c5,c1]
#結果を表示
print('組み合わせ数=',num_pattern)
c10,c5,c1=min_comb
print('最小枚数の組み合わせ＝',f'10円*{c10}+5円*{c5}+1円*{c1}')
c10,c5,c1=max_comb
print('最大枚数の組み合わせ＝'f'10円*{c10}+5円*{c5}+1円*{c1}')