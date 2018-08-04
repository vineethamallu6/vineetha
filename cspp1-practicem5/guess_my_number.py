print("think of a number between 0 to 100")
low=0
high=100
ans=int((high+low)/2)
print("Is your secret number =",str(ans) + "?")
i=input("Enter input h ig guess is too high,\
Enter input l if guess is too low, E ter c if guess is correct")
while i!='c':
    if i=='l':
        low=ans
        ans=int((low+high)/2)
        print("Is your secret number =",str(ans) + "?")
        i=input("Enter input h ig gurss is too high.Enter input l if guess is too low, Enter c if guess is correct")

    if i=='h':
        high=ans
        ans=int((low+high)/2)
        print("Is your secret number =",str(ans) + "?")
        i=input("Enter input h ig gurss is too high.Enter input l if guess is too low, Enter c if guess is correct")
              
    else:
        print("I do not understand your input")
        i=input("Enter input h ig gurss is too high.Enter input l if guess is too low. Enter c if guess is correct")

if i=='c':
    print("Game Over.your secret number is=",str(ans))
    
    

    
    
