import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    # for i, v in enumerate(lines):
    #     print("line[{0}]: {1}".format(i, v))
    n,k=map(int, lines[0].split())
    s=list(lines[1])
    if s.count('S')==0:
        print(n)
    else:
        while k:
            if s.count('S')==0:
                break
            elif 'SSS' in "".join(s):
                tmp="".join(s).index('SSS')
                s[tmp:tmp+3]='...'
                k-=1
            elif 'SS' in "".join(s):
                tmp="".join(s).index('SS')
                s[tmp:tmp+2]='..'
                k-=1
            elif 'S' in "".join(s):
                tmp="".join(s).index('S')
                s[tmp]='.'
                k-=1
            else:
                break

        result=s.count('.')
        print(result)


if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
