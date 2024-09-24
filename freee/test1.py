def solution(allowances, extraAllowances):
    # 元々最も多くのお小遣いを持っていた子どもの金額を見つける
    max_allowance = max(allowances)
    
    # 判定結果を格納するリスト
    result = []
    
    # 各子どもに extraAllowances を追加した後の金額を計算し、判定する
    for allowance in allowances:
        if allowance + extraAllowances > max_allowance:
            result.append(True)
        else:
            result.append(False)
    
    return result

# 使用例
allowances = [10, 20, 30, 40]
extraAllowances = 15
print(solution(allowances, extraAllowances))  # 出力: [False, False, True, True]