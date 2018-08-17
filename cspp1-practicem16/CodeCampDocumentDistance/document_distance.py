'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILE = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list1 = dict1.split(' ')
    list2 = dict2.split(' ')
    l_3 = list1 + list2
    dicti = {}
    for word in l_3:
        if word not in load_stopwords(FILE).keys():
            if word not in "!@#$%^&*()_+":
                dicti[word] = (dict1.count(word), dict2.count(word))
    num = 0
    sum1 = 0
    sum2 = 0
    dem = 0
    res = 0
    for word in dicti:
        num += dicti[word][0] * dicti[word][1]
        sum1 += dicti[word][0] ** 2
        sum2 += dicti[word][1] ** 2
    dem = math.sqrt(sum1) * math.sqrt(sum2)
    res = num / dem
    return res


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
    input1.lower()
    input2.lower()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
