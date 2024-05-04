from collections import Counter

s=input()
c=Counter(s)
d=Counter(c.values())
if set(d.values())==set([2]):
    print("Yes")
else:
    print("No")