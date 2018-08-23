def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    result = [[0 for row in range(len(m1))] for col in range(len(m2[0]))]
    for row in range(len(m1)):
        for col in range(len(m2[0])):
           for k_1 in range(len(m2)):
               result[row][col] += m1[row][k_1] * m2[k_1][col]
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
    for row in range(len(m1)):
        for col in range(len(m1[0])):
            result[row][col] = m1[row][col] + m2[row][col]
    return result

def read_matrix():
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    row,col = map(int,input().strip().split(","))
    matrix = []
    for i in range(row):
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
