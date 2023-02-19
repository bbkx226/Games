from random import randrange

def display_board(board):
    for i in range(0,len(board),3):
        print("+-------"*3 + "+")
        print("|       "*3 + "|")
        print("|   " + str(board[i]) + \
                 "   |   " + str(board[i + 1]) + \
                "   |   " + str(board[i + 2]) + "   |   ")
        print("|       "*3 + "|")
    print("+-------"*3 + "+")

def enter_move(board):
    freeFields = make_list_of_free_fields(board)
    pos = int(input("Enter your move:"))

    while(pos < 1 or pos > 9):
        print("Please enter number between 1 ~ 9")
        pos = int(input("Enter your move:"))
        
    while True:
        if pos in freeFields:
            board[pos - 1] = 'O'
            break
        else:
            print('Position already filled')
            pos = int(input("Enter your move:"))
    display_board(board)



def make_list_of_free_fields(board):
    free = []
    for i in range(len(board)):
            if board[i] != 'O' and board[i]!='X':
                free.append(board[i])
    return free

def victory_for(board, sign):
    arrangements = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for i in range(len(arrangements)):
        pos1, pos2, pos3 = arrangements[i][0] - 1, arrangements[i][1] - 1, arrangements[i][2] - 1
        if (str(board[pos1]) == sign) and (str(board[pos2]) == sign) and (str(board[pos3]) == sign):
            return True
    return False


def draw_move(board):
    freeFields = make_list_of_free_fields(board)
    pos = randrange(1,10)
    while True:
        if pos in freeFields:
            board[pos - 1] = 'X'
            break
        else:
            pos = randrange(1, 10)
    display_board(board)
    
board = [1, 2, 3, 4, 'X', 6, 7, 8, 9]

display_board(board)
while True:
    #check if all board field is filled
    moves = 0
    for i in range(len(board)):
        if board[i] == 'O' or board[i] =='X':
            moves +=1
    if moves == len(board):
        print('Game is Tie')
        break

    # user turn
    enter_move(board)
    if victory_for(board, 'O'):
        print('You won!!!')
        break
    # computer turn
    draw_move(board)
    if victory_for(board, 'X'):
        print('Computer won!!!')
        break
