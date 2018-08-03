"'#TAKING THE INPUT'"
STR = input("enter a string=")
VOWELS = 0
"'#CHECKING THE RANGE'"
for i in STR:
    if i in'aeiou':
        VOWELS = VOWELS + 1
print("number of vowels=", VOWELS)
