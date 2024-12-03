N, D = map(int, input().split())
S = input()

cookie_count = S.count('@')

empty_boxes = N - (cookie_count - D)

print(empty_boxes)