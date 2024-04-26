S=input()

if S[0]=="<"and S[-1]==">":
    for i in range(1,len(S)-1):
        if S[i]!="=":
            print("No")
            exit()
    print("Yes")
else:
    print("No")