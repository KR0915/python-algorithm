N,M=map(int,input().split())
shop=[]
shop_masks = []
for _ in range(N):
    S=input()
    shop.append(S)


for shop in shop:
        mask = 0
        for j in range(M):
            if shop[j] == 'o':
                mask |= (1 << j)
        shop_masks.append(mask)
        


full_mask = (1 << M) - 1

min_shops = N
for subset in range(1 << N):
    combined_mask = 0
    count = 0
    for i in range(N):
        if subset & (1 << i):
            combined_mask |= shop_masks[i]
            count += 1
    if combined_mask == full_mask:
        min_shops = min(min_shops, count)
    
print(min_shops)
            
