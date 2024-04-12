#1からnまでの合計を求める関数
def rec_sum(n):
    if n<=1:
        return 1
    return n+rec_sum(n-1)
print(rec_sum(10))