import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    step=int(lines[0])

    if step==1:
        product=int(lines[1])

        stock={}

        for i in range(2,product+2):
            D,S,P=lines[i].split()
            stock[int(D)]=int(S)

        result=[]

        for j in range(product+2,len(lines)):
            a=lines[j].split()
            T=int(a[1])
            D=int(a[2])
            N=int(a[3])

            if D in stock and stock[D]>=N:
                stock[D]-=N
                for k in range(N):
                    result.append(f"received order {T} {D}")
            else:
                result.append(f"sold out {T}")

        for k in result:
            print(k)

    elif step==2:
        a=lines[1].split()
        M=int(a[0])
        K=int(a[1])
        r=[]
        d=[]
        result=[]

        for j in range(M+2,len(lines)):
            b=lines[j].split()
            if b[0]=='received':
                T=int(b[2])
                D=int(b[3])
                d.append(D)
                if len(r)<K:
                    r.append(int(d[0]))
                    result.append(int(d[0]))
                else:
                    result.append('wait')
            elif b[0]=='complete':
                D=int(b[1])
                if D in r and len(d)==0:
                    result.append('ok')
                    d.pop(0)
                elif D in r:
                    d.pop(0)
                    r.pop(0)
                    if d:
                        result.append(f"ok {d[0]}")
                    if len(d)>0:
                        r.append(d[0])
                else:
                    result.append('unexpected input') 
        
        for result in result:
            print(result)
        



if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
