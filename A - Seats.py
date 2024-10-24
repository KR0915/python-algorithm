N=int(input())
S=input()
counter=0
for i in range(N-2):
    if S[i:i+3]=='#.#':
        counter+=1
print(counter)