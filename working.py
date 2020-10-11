board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

board2 = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

# recursive function to solve sudoku using helper functions
def solve(board):

    found = find_empty(board)

    # found a solution or not
    if not (found):
        return True
    else:
        row, column = found

    for i in range(1,10): # iterate from 1-9
        if valid_board(board, i, (row, column)): # when parameters are valid, set cell to i
            board[row][column] = i

            if solve(board): # recursively solve our problem until we get a solution
                return True
            
            board[row][column] = 0 # backtrack and reset the element we modified to 0
    
    return False
    

# validate that the board is a correctly formatted board
def valid_board(board, number, position):
    # check each element in row
    for i in range(len(board[0])): 
        if board[position[0]][i] == number and position[1] != i: # check if pos is same as number just added in
            return False

    # check columns
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i: 
            return False

    # check each 3x3 section
    box_x = position[1] // 3 # {0, 1, 2}
    box_y = position[0] // 3 # {0, 1, 2}

    """
    box values range from 0-2 -> multiply by 3 to get to 
    correct box based on position.
    Loop through indexed box up to but not including the outside
    perimeter.
    """
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] ==  number and (i,j) != position:
                return False
    
    return True

# find first empty cell occurrence
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0: # when cell is 0
                return (i,j) #return x,y pos tuple
    
    return None

# print sudoku board
def print_board(board):
    # every 3rd row prints horizontal line
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        # every pos in row
        for j in range(len(board[0])):
            # print vertical line for 3rd column
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # last pos with \n condition
            if j == 8:
                print(board[i][j])
            # normal pos -> print num and space
            else:
                print(str(board[i][j]) + " ", end="")

print_board(board)
solve(board)
print()
print("Our solution below")
print()
print_board(board)