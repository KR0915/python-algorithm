from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
ans=[]

def find_char_positions(text):
    char_positions = defaultdict(list)
    for index, char in enumerate(text):
        char_positions[char].append(index)
    return char_positions

positions = find_char_positions(A)

last_seen = defaultdict(lambda: -1)
for i, num in enumerate(A):
    if last_seen[num] != -1:
        ans.append(int(last_seen[num])+1)
    else:
        ans.append(-1)
    last_seen[num] = i
    
print(" ".join(map(str, ans)))