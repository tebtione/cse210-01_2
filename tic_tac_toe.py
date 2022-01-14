# Tic Tac Toe game

""" Tic Tac Toe game
    Author: Time (Tech With Tim)
    I edited a few....
"""

board = [' ' for x in range(10)]


def insertBoard(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '



def isWinner(bo, le):

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[1] == le and bo[4] == le and bo[7] == le) or # down the left side
    (bo[2] == le and bo[5] == le and bo[8] == le) or # down the middle
    (bo[3] == le and bo[6] == le and bo[6] == le) or # down the right side
    (bo[1] == le and bo[5] == le and bo[9] == le) or # diagonal
    (bo[3] == le and bo[5] == le and bo[7] == le)) # diagonal

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an X (1-9)')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertBoard('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within te range!')
        except:
            print('Please type a number')

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 0 in possibleMoves:
        move = 0
        return move

    #Take any edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
    
    return move


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def main():
    print('Welcome to Tic Tao Toe')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, '0')):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, '0's won this time!")
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertBoard('o', move)
                print('Computer placed an o in position', move, ':')
                printBoard(board)
        else:
            print("'X's won this time! Good job!")
            break

    if isBoardFull(board):
        print('Tie Game!')

main()

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break

