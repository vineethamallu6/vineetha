'''
    Document Distance - A detailed description is given in the PDF
'''
import re
stopwords = "stopwords.txt"
def cleanup_words(input1):
    reg = re.compile('[^a-z]')
    input1 = input1.lower().split(' ')
    input1 = [reg.sub('',w.strip())for w in input1]
    return input1
def remove_words(input1,input2):
    d = {}
    d = load_stopwords(stopwords)
    word_list1 = cleanup_words(input1)
    word_list2 = cleanup_words(input2)
    word_list = word_list1 + word_list2
    dictionary = {}
    for word in word_list:
        if word not in d.keys() and len(word)>0:
            dictionary[word] = (word_list1.count(word),word_list2.count(word))
    return dictionary
import math
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    dictionary = {}
    dictionary = remove_words(dict1,dict2)
    num = 0
    dem = 0
    sum1 = 0
    sum2 = 0
    for dictionary in dictionary.values():
        num = num + (dictionary[0]*dictionary[1])
        sum1 += dictionary[0] ** 2
        sum2 += dictionary[1] ** 2
    dem = math.sqrt(sum1) * math.sqrt(sum2)
    return (num/dem)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()

    print(similarity(input1,input2))

if __name__ == '__main__':
    main()
