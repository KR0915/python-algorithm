def kaijou(n):
    result=1
    for a in range(1,n+1):
        result*=a
    print(result)
    
num1=int(input("数値を入力してください"))
kaijou(num1)