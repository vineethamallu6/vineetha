"'# input a value'"
def factorial(num):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n.
    '''
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)
def main():
    '''
    main function
    '''
    ans = input()
    print(factorial(int(ans)))    
if __name__ == "__main__":
    main()
