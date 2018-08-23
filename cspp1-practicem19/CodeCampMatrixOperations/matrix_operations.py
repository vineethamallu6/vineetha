def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = [[0 for row in range(len(m1))] for col in range(len(m2[0]))]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
           for k in range(len(m2)):
               result[i][j] += m1[i][k] * m2[k][j]
    return result

def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result = [[0 for row in range(len(m1))] for col in range(len(m2[0]))]
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            result[i][j] = m1[i][j] + m2[i][j]
    return result

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    n,m = map(int,input().strip().split(","))
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().rstrip().split())))
    return matrix
            
    



def main():
    # read matrix 1

    # read matrix 2
    matrix1 = []
    matrix1 = read_matrix()
    matrix2 = []
    matrix2 = read_matrix()
    print(add_matrix(matrix1, matrix2))
    print(mult_matrix(matrix1, matrix2))

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2
    pass

if __name__ == '__main__':
    main()
