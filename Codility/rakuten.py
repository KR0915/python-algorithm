def solution(A):
    # 線分の長さの頻度をカウントし辞書に格納
    count_A = {}
    for length in A:
        if length in count_A:
            count_A[length] += 1
        else:
            count_A[length] = 1
    
    # 結合可能な線分の長さを降順で取得
    lengths = sorted(count_A.keys(), reverse=True)
    max_squares = 0
    
    for length in lengths:
        # 4本の長さが同じ線分を使って正方形を作れる場合
        if count_A[length] >= 4:
            max_squares = max(max_squares, length)
            count_A[length] -= 4
        # 2本の長さが同じ線分を使って他の2本の線分と合わせて正方形を作れる場合
        elif count_A[length] >= 2:
            for shorter in lengths:
                if shorter < length and count_A[shorter] >= 2:
                    max_squares = max(max_squares, min(length, shorter))
                    count_A[length] -= 2
                    count_A[shorter] -= 2
                    break
                
            for shorter in lengths:
                if shorter < length and count_A[shorter] >= 1:
                    max_squares = max(max_squares, min(length, shorter))
                    count_A[length] -= 2
                    count_A[shorter] -= 1
                    break
                
        # 1本の長さが同じ線分を使って他の3本の線分と合わせて正方形を作れる場合
        elif count_A[length] >= 1:
            for shorter in lengths:
                if shorter < length and count_A[shorter] >= 3:
                    max_squares = max(max_squares, min(length, shorter))
                    count_A[length] -= 1
                    count_A[shorter] -= 3
                    break
            # 1本の長さが同じ線分を使って他の2本の線分と合わせて正方形を作れる場合
            for shorter in lengths:
                if shorter < length and count_A[shorter] >= 2:
                    max_squares = max(max_squares, min(length, shorter))
                    count_A[length] -= 1
                    count_A[shorter] -= 2
                    break
    
    return max_squares