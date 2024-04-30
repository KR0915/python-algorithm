A=input()
result=[]
for i in range(len(A)):
    if A[i]=='|':
        result.append(i)

A=A.replace(A[result[0]:result[1]+1],'')
print(A)