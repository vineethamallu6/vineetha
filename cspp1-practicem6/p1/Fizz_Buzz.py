n=int(input())
for i in range(n+1):
    while i>0:
        if i%3==0 and i%5==0:
            print("Fizz")
            print("Buzz")
            break
        if i%3==0:
            print("Fizz")
            break
        elif i%5==0:
            print("Buzz")
            break
        print(i)
        break
    i=i+1       
