'''import'''
import re
def clean_string(string):
    '''cleaning words'''
    reg = re.compile('[^[a-z,A-Z,0-9]')
    string = reg.sub('', string.strip())
    return string

def main():
    '''main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
