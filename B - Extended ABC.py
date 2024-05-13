S=input()
for i in range(len(S)-1):
    if (S[i]+S[i+1])=='AC' or (S[i]+S[i+1])=='BA' or (S[i]+S[i+1])=='CA' or (S[i]+S[i+1])=='CB':
        print('No')
        break
else:
    print('Yes')
        
        