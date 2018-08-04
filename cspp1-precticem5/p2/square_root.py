"'enter the input'"
SQ = int(input())
EPS = 0.01
I = 0.0
INCREMENT = 0.1
while abs(I**2 - SQ) >= EPS:
    I += INCREMENT
if abs(I**2 - SQ) >= EPS:
    print('failed')
else:
    print(I)

        
