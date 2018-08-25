'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''cleaning words'''
    reg = re.compile('[^!@#$%^&*()_+]')
    string = reg.sub('',string)
    return string

def main():
    '''main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
