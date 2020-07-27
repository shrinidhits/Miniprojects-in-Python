def print_board(bo):
    for i in range(9):
        if i%3==0 and i!=0:
            print("----------------------------------")
        for j in range(9):
            if j%3==0 and j!=0:
                print(" | ",end="")
            if j==8:
                print(" "+str(bo[i][j]))
            else:
                print(" "+str(bo[i][j])+" ",end="")
    print("\n")
def empty_location(bo,l):
    for i in range(9):
        for j in range(9):
            if bo[i][j]==0:
                l[0]=i
                l[1]=j
                return True
    return False

def over_in_row(bo,num,row):
    for i in range(9):
        if bo[row][i]==num:
            return True
    return False

def over_in_col(bo,num,col):
    for i in range(9):
        if bo[i][col]==num:
            return True
    return False

def over_in_box(bo,num,row,col):
    for i in range(3):
        for j in range(3):
            if bo[i+row][j+col]==num:
                return True
    return False

def check(bo,num,row,col):
    return not over_in_row(bo,num,row) and not over_in_col(bo,num,col) and not over_in_box(bo,num,row-row%3, col-col%3)


def solve_sudoku(bo):
    l=[0,0]

    if not empty_location(bo,l):
        return True
    row=l[0]
    col=l[1]

    for i in range(1,10):
        if check(bo,i,row,col):
            bo[row][col]=i
            if solve_sudoku(bo):
                return True
            else:
                bo[row][col]=0
    return False


if __name__=="__main__":
    board= [
        [0, 2, 0, 0, 6, 0, 0, 0, 8],
        [0, 0, 1, 0, 0, 0, 0, 4, 0],
        [0, 0, 7, 0, 8, 5, 6, 2, 0],
        [7, 0, 3, 0, 0, 4, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 5, 0, 0],
        [0, 0, 0, 6, 0, 0, 4, 0, 1],
        [0, 3, 6, 5, 7, 0, 9, 0, 0],
        [0, 9, 0, 0, 0, 0, 7, 0, 0],
        [1, 0, 0, 0, 4, 0, 0, 5, 0]
    ]
    print_board(board)
    if solve_sudoku(board):
        print("Solution:\n")
        print_board(board)
    else:
        print("Not possible")