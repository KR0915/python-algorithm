N,Q=map(int,input().split())
instructions = [input().split() for _ in range(Q)]
left_hand = 1
right_hand = 2
total_moves = 0
for H, T in instructions:
    T = int(T)
    if H == 'L':
        if T != right_hand:
            if left_hand<right_hand<T:
                distance=N - abs(left_hand - T)
            elif T<right_hand<left_hand:
                distance=N - abs(left_hand - T)
            elif left_hand<right_hand and T<left_hand:
                distance=N - abs(left_hand - T)
            elif left_hand>right_hand and T>left_hand:
                distance=abs(left_hand - T)
            elif left_hand<T<right_hand:
                distance=abs(left_hand - T)
            else:
                distance = min(abs(left_hand - T), N - abs(left_hand - T))
            print(distance)
            total_moves += distance
            left_hand = T
    elif H == 'R':
        if T != left_hand:
            if right_hand<left_hand<T:
                distance=N - abs(right_hand - T)
            elif T<left_hand<right_hand:
                distance=N-abs(right_hand - T)
            elif right_hand<left_hand and T<right_hand:
                distance=N - abs(right_hand - T)
            elif right_hand>left_hand and T>right_hand:
                distance=abs(right_hand - T)
            else:
                distance = min(abs(right_hand - T), N - abs(right_hand - T))
            
            print(distance)
            total_moves += distance
            right_hand = T

print(total_moves)
