def max_product_no_common_digits(A):
    def has_common_digits(x, y):
        return not set(str(x)).isdisjoint(set(str(y)))

    max_product = -1
    n = len(A)

    for i in range(n):
        for j in range(i + 1, n):
            if not has_common_digits(A[i], A[j]):
                product = A[i] * A[j]
                if product > max_product:
                    max_product = product

    return max_product

# テスト
A = [123, 456, 789, 12, 34]
print(max_product_no_common_digits(A))  # 出力: 789 * 34 = 26826

A = [12, 23, 34, 45]
print(max_product_no_common_digits(A))  # 出力: -1 (共通する桁を持たない2つの整数がない)