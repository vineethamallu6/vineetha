"'#TAKING THEINPUT'"
STR = input()
COUNT = 0
LEN = int(len(STR))
i = 0
j = 3
"'#CHECKING THE RANGE'"
while j <= LEN:
    C = STR[i:j]
    if C == "bob":
        COUNT = COUNT+1
    i = i+1
    j = j+1
print(COUNT)
