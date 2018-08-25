'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    string = ""
    n = int(input())
    for i in range(n):
        i += 1
        string += input()
        string += '\n'
    print(string)

if __name__ == '__main__':
    main()
