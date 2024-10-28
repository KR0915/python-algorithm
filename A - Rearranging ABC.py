def can_rearrange_to_ABC(S):
    return sorted(S) == ['A', 'B', 'C']

S = input().strip()


if can_rearrange_to_ABC(S):
    print("Yes")
else:
    print("No")