def max_11_22_substring(N, S):
    max_length = 0
    left_ones = [0] * N
    right_twos = [0] * N

    count = 0
    for i in range(N):
        if S[i] == '1':
            count += 1
        else:
            count = 0
        left_ones[i] = count

    count = 0
    for i in range(N - 1, -1, -1):
        if S[i] == '2':
            count += 1
        else:
            count = 0
        right_twos[i] = count

    for i in range(N):
        if S[i] == '/':
            left_count = left_ones[i - 1] if i > 0 else 0
            right_count = right_twos[i + 1] if i < N - 1 else 0
            max_length = max(max_length, 1 + 2 * min(left_count, right_count))

    return max_length

N = int(input())
S = input()
print(max_11_22_substring(N, S))
