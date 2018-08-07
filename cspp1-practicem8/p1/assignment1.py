def factorial(n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def main():
    a = input()
    print(factorial(int(a)))    

if __name__== "__main__":
    main()
