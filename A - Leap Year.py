Y=int(input())
if Y%4!=0:
    print(365)
elif Y%100!=0 and Y%4==0:
    print(366)
elif Y%400!=0 and Y%100==0:
    print(365)
elif Y%400==0:
    print(366)