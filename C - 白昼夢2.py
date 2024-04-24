def can_convert(S):
    while S:
        if S.endswith("dream"):
            S = S[:-5]
        elif S.endswith("dreamer"):
            S = S[:-7]
        elif S.endswith("erase"):
            S = S[:-5]
        elif S.endswith("eraser"):
            S = S[:-6]
        else:
            return False
    return True


S = input()
if can_convert(S):
    print("Yes")
else:
    print("No")