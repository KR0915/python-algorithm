n = int(input())
s = input()
point = 0

# 100の位
for i in range(10):
    # Sのn-2番目までにiがあるか
    str_i = str(i)
    for a in range(n-2):
        if s[a] == str_i:
            now_i = a
            break
    # 作れなかった場合打ち切り
    else:
        continue
    # 10の位
    for j in range(10):
        str_j = str(j)
        for b in range(now_i+1,n-1):
            if s[b] == str_j:
                now_j = b
                break
        else:
            continue
        # 1の位
        for k in range(10):
            str_k = str(k)
            for c in range(now_j+1,n):
                # 暗証番号がそろった
                if s[c] == str_k:
                    point += 1
                    break

print(point)