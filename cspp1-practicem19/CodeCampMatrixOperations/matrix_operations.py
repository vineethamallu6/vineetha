'''multiplication'''
def mult_matrix(mat1, mat2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(mat1[0]) == len(mat2):
        result = [[0 for row in range(len(mat1))] for col in range(len(mat2[0]))]
        for row in range(len(mat1)):
            for col in range(len(mat2[0])):
                for k_1 in range(len(mat2)):
                    result[row][col] += mat1[row][k_1] * mat2[k_1][col]
        return result
    else:
        print("Error: Matrix shapes invalid for mult")
        return None
def add_matrix(mat1, mat2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    result = [[0 for col in range(len(mat1[0]))] for row in range(len(mat1))]
    if len(mat1) == len(mat2) and len(mat1[0]) == len(mat2[0]):
        for row in range(len(mat1)):
            for col in range(len(mat1[0])):
                result[row][col] = mat1[row][col] + mat2[row][col]
        return result
    else:
        print("Error: Matrix shapes invalid for addition")
        return None
def read_matrix(row, col):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    matrix = []
    for i in range(row):
        i += 1
        input1 = input().split(' ')
        if len(input1) == col:
            matrix.append(list(map(int, input1)))
        else:
            print("Error: Invalid input for the matrix")
            return None
    return matrix
def main():
    ''' read matrix'''
    row, col = map(int, input().split(','))
    matrix1 = read_matrix(row, col)
    if matrix1 is None:
        exit(0)
    row, col = map(int, input().split(','))
    matrix2 = read_matrix(row, col)
    if matrix2 is None:
        exit(0)
    print(add_matrix(matrix1, matrix2))
    print(mult_matrix(matrix1, matrix2))
    # add matrix 1 and matrix 2
    # multiply matrix 1 and matrix 2
if __name__ == '__main__':
    main()
