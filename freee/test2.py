def solution(intervals):
    if not intervals:
        return []

    # 開始時間でソート
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []
    current_interval = intervals[0]
    print(intervals[1:])

    for next_interval in intervals[1:]:
        print(current_interval[1],next_interval[0])
        if current_interval[1] >= next_interval[0]:
            # 重複している場合、間隔をマージ
            current_interval[1] = max(current_interval[1], next_interval[1])
        else:
            # 重複していない場合、現在の間隔を結果リストに追加
            merged_intervals.append(current_interval)
            current_interval = next_interval

    # 最後の間隔を追加
    merged_intervals.append(current_interval)

    return merged_intervals

# 使用例
intervals1 = [[1, 3], [2, 4], [5, 7]]
print(solution(intervals1))  # 出力: [[1, 4], [5, 7]]

intervals2 = [[1, 2], [2, 3], [3, 4]]
print(solution(intervals2))  # 出力: [[1, 4]]