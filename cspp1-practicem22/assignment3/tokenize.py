'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
	'''token'''
    dict1 = {}
    word1 = []
    string=string.split(' ')
    for line in string:
        word1.append(line)
    for word in word1:
        if word not in dict1.keys():
            dict1[word] = ((i, j.count(j)) for i,j in enumerate(word1) )
    return dict1


            
def main():
	'''main'''
    string=""
    num=int(input())
    for i in range(num):
        i += 1
        string += input()
        string += '\n'
        print(tokenize(string))

if __name__ == '__main__':
    main()
