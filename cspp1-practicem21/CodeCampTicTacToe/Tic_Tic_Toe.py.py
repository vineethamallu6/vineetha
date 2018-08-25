'''function'''
def tictactoe(matrix):
    '''checking condition'''
    win = []
    for i in matrix:
        if i[0] == i[1] == i[2]:
            win.append(i[0])
    for j in range(0, 3):
        if matrix[0][j] == matrix[1][j] == matrix[2][j]:
            win.append(matrix[0][j])
    if matrix[0][0] == matrix[1][1] == matrix[2][2]:
        win.append(matrix[0][0])
    if matrix[2][0] == matrix[1][1] == matrix[0][2]:
        win.append(matrix[0][2])
    if win == []:
        print('draw')
        return None
    if len(win) == 1:
        if win[0] == 'x' or win[0] == 'o':
            print(win[0])
        else:
            print('invalid input')
        return None
    else:
        print('invalid game')
        return None
def main():
    '''main function'''
    matx = []
    for _ in range(0, 3):
        col = input().split(' ')
        matx.append(col)
    tictactoe(matx)
if __name__ == '__main__':
    main()
