N = int(input())
for I in range(N+1):
    while I>0:
        if I%3 == 0 and I%5 == 0:
            print("Fizz")
            print("Buzz")
            break
        if I%3 == 0:
            print("Fizz")
            break
        elif I%5 == 0:
            print("Buzz")
            break
        print(I)
        break
    I = I+1       
