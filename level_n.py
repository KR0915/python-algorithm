import sys
import math

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))
    l,r=map(int, lines[0].split())
    m=int(lines[1])
    n = list(map(int, lines[2].split()))
    
    count=0
    for i in range(l,r+1):
        if m==1 and 1 in n:
            break
        elif all(i%x!=0 for x in n):
            count+=1

    print(count)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
