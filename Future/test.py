import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    b=lines[0].split()
    n=int(b[0])
    x=int(b[1])
    y=list(map(int,lines[1].split()))
    flag=True
    for i in range(len(y)):
        if y[i]<x:
            flag=False

    if flag:
        print('Alcohol')
    else:
        print('Soft Drink')


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)