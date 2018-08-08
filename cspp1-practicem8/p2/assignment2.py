"'# input a value'"
def sumofdigits(num):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    '''
    if num == 0:
        return 0
    else:
        return ((num%10) + sumofdigits(num//10))
def main():
    ans = input()
    print(sumofdigits(int(ans)))  

if __name__ == "__main__":
    main()

