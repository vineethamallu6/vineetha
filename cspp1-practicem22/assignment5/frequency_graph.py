'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    string=""
    for d in dictionary.keys():
        value=dictionary[d]
    for i in range(value):
        string+="#"
    for key, value in sorted(dictionary.items()):
        print(key, "-",string )
        
    

def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
