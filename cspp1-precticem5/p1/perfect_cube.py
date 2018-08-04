"'#enter the input'"
CUBE = int(input())
for I in range(abs(CUBE) + 1):
    if I ** 3 >= abs(CUBE):
        break
if I ** 3 != abs(CUBE):
    print(str(CUBE) + ' is not a perfect number')
else:
    if CUBE < 0:
        I -= 1
    print(str(CUBE)+ ' is a perfect cube')
