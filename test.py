def max_11_22_substring_length(S):
    N = len(S)
    max_length = 0

    for left in range(N):
        if S[left] == '1':
            right = left
            while right < N and S[right] == '1':
                right += 1
            if right < N and S[right] == '/':
                mid = right
                right += 1
                while right < N and S[right] == '2':
                    right += 1
                if right - left == 2 * (mid - left) + 1:
                    max_length = max(max_length, right - left)
        left += 1

    return max_length

# 入力の読み込み
N = int(input())
S = input()

# 最大部分文字列の長さを求める
result = max_11_22_substring_length(S)
print(result)