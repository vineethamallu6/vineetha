"'#enter the input'"
SQ = int(input())
EPS = 0.01
LOW = 1.0
HIGH = SQ
RES = (HIGH+LOW)/2.0
while abs(RES**2 - SQ) >= EPS:
    if RES**2 < SQ:
        LOW = RES
    else:
        HIGH = RES
    RES = (HIGH+LOW)/2.0
print(RES)
