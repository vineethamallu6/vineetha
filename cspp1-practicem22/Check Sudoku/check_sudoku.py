'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''for i in sudoku:
            if list(set(i[0]=='1-9')):
            return True
        return False

def main():
    '''
    main
    '''
    sudoku = []
    for i in range(9):
        row = input().split(' ')
        sudoku.append(row)
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()
