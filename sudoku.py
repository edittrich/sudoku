import random

levels = {
    "einfach": 65,
    "normal": 29,
    "schwer": 26
}

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


def validate(y, x):
    n = board[y][x]
    for i in range(0, 9):
        if board[y][i] == n and x != i:
            return False

    for i in range(0, 9):
        if board[i][x] == n and y != i:
            return False

    for i in range(y // 3 * 3, y // 3 * 3 + 3):
        for j in range(x // 3 * 3, x // 3 * 3 + 3):
            if board[i][j] == n and y != i and x != j:
                return False

    return True


def solve(y, x):
    if y == 9:
        return True

    x_new = (x + 1) % 9
    y_new = (y * 9 + x + 1) // 9

    if board[y][x] > 0:
        return solve(y_new, x_new)
    else:
        for n in range(1, 10):
            board[y][x] = n
            if validate(y, x):
                if solve(y_new, x_new):
                    return True

        board[y][x] = 0
        return False


def create(y, x):
    if y == 9:
        return True

    x_new = (x + 1) % 9
    y_new = (y * 9 + x + 1) // 9

    list_n = list(range(1, 10))

    for i in range(0, 9):
        if board[y][i] in list_n:
            list_n.remove(board[y][i])

    for i in range(0, 9):
        if board[i][x] in list_n:
            list_n.remove(board[i][x])

    for i in range(y // 3 * 3, y // 3 * 3 + 3):
        for j in range(x // 3 * 3, x // 3 * 3 + 3):
            if board[i][j] in list_n:
                list_n.remove(board[i][j])

    for i in range(0, len(list_n)):
        n = list_n[random.randint(0, len(list_n)) - 1]
        board[y][x] = n
        list_n.remove(n)
        if validate(y, x):
            if create(y_new, x_new):
                return True

    board[y][x] = 0
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
    board = list(board_00)
    create(0, 0)
    visualize()
    solve(0, 0)
    visualize()
