"'#enter the input'"
EP = 0.01
Y = int(input())
X = Y/2.0
while abs(X*X - Y) >= EP:
    X = X - (((X**2)-Y)/(2*X))
print(X)