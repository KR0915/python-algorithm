Q = int(input())
bag = []
bag_set = set()
ans = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if len(query) == 1:
        q = 3
    else:
        q = query[0]
        x = query[1]
        
    if q == 1:
        bag.append(x)
        bag_set.add(x)
    elif q == 2:
        if x in bag_set:
            bag.remove(x)
            bag_set.remove(x)
    else:
        ans.append(len(bag_set))

print("\n".join(map(str, ans)))