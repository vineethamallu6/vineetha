"'input number'"
NUM = int(input())
MUL = 1
while NUM > 0:
    TEMP = NUM%10
    MUL = MUL*TEMP
    NUM = NUM//10
print(MUL)
