'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    string=""
    value=0
    co=[]
    for d in dictionary.keys():
        value=dictionary[d]
        co.append(value)
    print(d)
    for i in co:
        string=string+"#"
    for key, value in sorted(dictionary.items()):
        print(key, "-", string)
        
    

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
