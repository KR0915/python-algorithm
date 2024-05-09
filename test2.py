A=list(input())
print(A)
a=[]
s=[]
for value in A:
    try:
        converted_value = int(value)
        a.append(converted_value)
    except ValueError:
        s.append(value) 
        
print(a)
print(s)

if a[-1]%a[1]==0: