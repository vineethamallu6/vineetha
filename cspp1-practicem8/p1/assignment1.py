def factorial(num):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(n-1)
def main():
    '''
    main function
    '''
    a = input()
    print(factorial(int(a)))    
if __name__== "__main__":
    main()
