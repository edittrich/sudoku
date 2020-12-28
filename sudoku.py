board_00 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

board_01 = [
        [0, 0, 7, 0, 0, 0, 0, 0, 1],
        [0, 0, 8, 0, 0, 0, 4, 3, 0],
        [0, 0, 0, 0, 2, 1, 0, 5, 7],
        [0, 4, 0, 3, 0, 0, 0, 1, 0],
        [2, 0, 0, 0, 1, 0, 0, 0, 9],
        [0, 7, 0, 0, 0, 5, 0, 4, 0],
        [6, 1, 0, 5, 3, 0, 0, 0, 0],
        [0, 3, 9, 0, 0, 0, 1, 0, 0],
        [4, 0, 0, 0, 0, 0, 6, 0, 0]
    ]


def validate(y_sudoku, x_sudoku, digit):
    for i in range(0, 9):
        if board[y_sudoku][i] == digit and x_sudoku != i:
            return False

    for i in range(0, 9):
        if board[i][x_sudoku] == digit and y_sudoku != i:
            return False

    for i in range(y_sudoku // 3 * 3, y_sudoku // 3 * 3 + 3):
        for j in range(x_sudoku // 3 * 3, x_sudoku // 3 * 3 + 3):
            if board[i][j] == digit and y_sudoku != i and x_sudoku != j:
                return False

    return True


def solve(y_sudoku, x_sudoku):
    if y_sudoku == 9:
        return True

    if x_sudoku < 8:
        x_new_sudoku = x_sudoku + 1
        y_new_sudoku = y_sudoku
    else:
        x_new_sudoku = 0
        y_new_sudoku = y_sudoku + 1

    if board[y_sudoku][x_sudoku] > 0:
        return solve(y_new_sudoku, x_new_sudoku)
    else:
        for digit in range(1, 10):
            board[y_sudoku][x_sudoku] = digit
            if validate(y_sudoku, x_sudoku, digit):
                if solve(y_new_sudoku, x_new_sudoku):
                    return True

        board[y_sudoku][x_sudoku] = 0
        return False


def visualize():

    for y in range(0, 9):
        if y == 0:
            print('┌───┬───┬───┐')
        elif y % 3 == 0:
            print('├───┼───┼───┤')

        for x in range(0, 9):
            if x == 0:
                print('│', end='')
            elif x % 3 == 0:
                print('│', end='')
            print(board[y][x], end='')
        print('│')

    print('└───┴───┴───┘')

    print('')


if __name__ == '__main__':
    board = list(board_01)
    visualize()
    solve(0, 0)
    visualize()
