def factorial(n):
    if n>0:
        return n*factorial(n-1)
    else:
        return 1
    
a=int(input('nを入力:'))
print(factorial(a))