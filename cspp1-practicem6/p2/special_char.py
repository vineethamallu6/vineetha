"'#input the string'"
STRING = input()
S = ' '
I = 0
for I in STRING:
    if I in'!@#$%^&*':
        I = ' '
    S += I
print(str(S))
