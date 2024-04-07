def get_nabeatu(num):
    if num%3==0:return'A'
    if'3'in str(num):return'A'
    return str(num)

for i in range(1,51):
    print(get_nabeatu(i))
