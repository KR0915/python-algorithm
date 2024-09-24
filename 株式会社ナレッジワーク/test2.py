import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    number=int(lines[0])

    digists=list(str(number))

    digists.sort()
    #ソートした結果一番最初が0の時、次に小さい整数を見つける。一番最初が0じゃなければソートした結果をそのまま出力する
    if digists[0]=='0':
        for i in range(1,len(digists)):
            if digists[i]!='0':
                digists[0],digists[i]=digists[i],digists[0]
                break

    min_number=''.join(digists)
    print(int(min_number))

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)