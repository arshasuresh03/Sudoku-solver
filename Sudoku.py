from random import sample


def generate_board(num_empty_cells):
    board_size = 9
    base = 3
    side = base * base

    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    def shuffle(s):
        return sample(s, len(s))

    r_base = range(base)
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, base * base + 1))

    board_tmp = [[nums[pattern(r, c)] for c in cols] for r in rows]

    for p in sample(range(side * side), side * side - num_empty_cells):
        board_tmp[p // side][p % side] = 0

    return board_tmp


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
    print("")


def possible(board, pos, num):
    row, col = pos

    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def next_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j
    return None


def solve(board):
    empty_slot = next_empty(board)
    if not empty_slot:
        return True
    else:
        row, col = empty_slot

    for num in range(1, 10):
        if possible(board, (row, col), num):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False


# Generate a new board with 0 empty cells
board = generate_board(0)

# Printing the unsolved board
print("====== Solvable Board ======")
print_board(board)

# Solving the board
solve(board)

# Printing the solved board
print("====== Solved Board ======")
print_board(board)
