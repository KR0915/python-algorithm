def main():
    S = input()
    N = len(S)
    
    sum = [[0] * (N + 1) for _ in range(26)]
    print(sum)
    for i in range(N):
        for j in range(26):
            sum[j][i + 1] = sum[j][i]
            print(sum[j][i + 1], sum[j][i])
        sum[ord(S[i]) - ord('A')][i + 1] += 1

    ans = 0
    for i in range(1, N - 1):
        for j in range(26):
            l = sum[j][i]
            r = sum[j][N] - sum[j][i + 1]
            print(l,r)
            ans += l * r

    print(ans)

if __name__ == "__main__":
    main()