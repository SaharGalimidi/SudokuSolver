board = [
    [2, 0, 0, 8, 0, 0, 0, 0, 0],
    [1, 0, 4, 7, 5, 0, 0, 0, 0],
    [0, 0, 6, 0, 1, 0, 9, 5, 0],
    [0, 2, 9, 0, 0, 3, 0, 0, 4],
    [0, 8, 0, 5, 0, 0, 0, 1, 0],
    [0, 7, 0, 0, 6, 2, 0, 0, 3],
    [9, 0, 5, 3, 0, 0, 4, 0, 8],
    [0, 0, 0, 0, 9, 0, 3, 0, 6],
    [3, 0, 0, 0, 7, 0, 0, 0, 0]
]


def solve(board):
    """
    Solve the sudoku using backtracking algorithm
    :param board: 2d list of integers
    :return: solution board
    """
    find = find_empty(board)
    if not find:  # We found a solution
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(board, num, (row, col)):  # Check if it is valid
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


def valid(bo, num, position):
    """
    Returns True if the given number is valid
    :param bo: 2d list of integers
    :param num: integer
    :param position: (row, col) a tuple with the coordinates of the num 0 in the board
    :return: boolean
    """

    # Check row
    for i in range(len(bo[0])):
        if bo[position[0]][i] == num:  # checking each element in the row
            return False

    # Check col
    for i in range(len(bo)):  # checking each element in the col
        if bo[i][position[1]] == num:
            return False

    # check subset board
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != position:
                return False

    return True


def print_board(board):
    """
    printing the board with subset of boards size 3x3
    :param board: 2d list of integers
    :return:None
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:  # print a horizontal line after 3 rows
            print("------------------------")
        for j in range(len(board[0])):  # print a vertical line after 3 cols
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:  # reach the end of the board
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    """
    finding an empty square in the board
    empty: value == 0
    :param board: 2d list of integers
    :return: tuple of the coordinates of the empty square
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col
    return None


print("Board before solution\n")
print_board(board)
if solve(board):
    print("Board after solution\n")
    print_board(board)
else:
    print("There is no solution to this sudoku")


