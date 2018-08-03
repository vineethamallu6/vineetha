"'#enter a string'"
S =  input()
SUB = S[0]
LEN = ' '
i=1
for i in range(1,len(S)):
    if SUB[-1] <= S[i]:
        SUB = SUB+S[i]
    else:
        if len(SUB)>len(LEN):
            LEN=SUB
        SUB=S[i]
    if len(SUB)>len(LEN):
        LEN=SUB
print(LEN)
