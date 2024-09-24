import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    N=int(lines[0])
    numbers=list(map(int,lines[1].split()))

    seen=set()
    #for文でループを回し、一度言われた正整数かどうかを判定する。
    #すでに正整数が言われていたら子供の順番を出力し、言われていなかったら、seenに正整数を保存する。
    for i in range(N):
        if numbers[i] in seen:
            print(i+1)
            return
        seen.add(numbers[i])

    print(-1)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)