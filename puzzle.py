

def is_valid(board, row, col, num):
    # Check the number in the row
    for x in range(9):
        if board[row][x] == num:
            return False

    # Check the number in the column
    for x in range(9):
        if board[x][col] == num:
            return False

    # Check the number in the box
    start_row, start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num

                        if solve_sudoku(board, n):
                            return True

                        board[i][j] = 0

                return False

    return True

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(board[i][j], end=" ")
        print()

# Example usage
n = 9
input_board = []
for i in range(n):
    row = list(map(int, input("Enter row {}: ".format(i+1)).split()))
    if len(row) != n:
        raise ValueError("Invalid row length")
    input_board.append(row)

if solve_sudoku(input_board, n):
    print_board(input_board)
else:
    print("No solution found!")