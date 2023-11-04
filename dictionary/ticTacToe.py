

theBoard = {"top_L": " ", "top_M": " ", "top_R": " ",
            "mid_L": " ", "mid_M": " ", "mid_R": " ",
            "low_L": " ", "low_M": " ", "low_R": " "}

def showBoard(board):
    print(board["top_L"] + '|' + board["top_M"] + '|' + board["top_R"])
    print('-----')
    print(board["mid_L"] + '|' + board["mid_M"] + '|' + board["mid_R"])
    print('-----')
    print(board["low_L"] + '|' + board["low_M"] + '|' + board["low_R"])

turn = 'X'
for i in range(9):
    move =  input("its {} TURN:. (move to which space?".format(turn))
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    showBoard(theBoard)

showBoard(theBoard)
