'''
Created on 20-Jan-2019

@author: vsrir
'''

def areMovesAvailable(board, whoseTurn, thisPlayerMoves):
    '''Local variable in order to NOT touch the player's actual moves'''
    testMoves = thisPlayerMoves[:]
    '''Create dummy moves in blank cells on the board and check if victory is possible'''
    for move in range(1,10):
        if board[(move-1)//3][(move-1)%3] == " ":
            testMoves.append(move)
            if checkVictory(testMoves, whoseTurn) == True:
                return True
    printBoard(board)
    return False

def checkVictory(playerMoves, whoseTurn):
    victoryOptions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    '''check if any set in victory options is available in current player moves'''
    for victoryOption in victoryOptions:
        victory = True
        for move in victoryOption:
            if move not in playerMoves:
                victory = False
                break
        if victory == True:
            return victory
    return False

def checkValidMove(board,thisMove):
    '''prevent bogus moves'''
    if not thisMove.isnumeric():
        print("Only numbers please. Try again.")
        return False       
    if not int(thisMove) in range(1,10):
        print("Invalid move. Try again.")
        return False
    if board[(int(thisMove)-1)//3][(int(thisMove)-1)%3] != " ":
        print("That cell is already taken. Try again.")
        return False
    return True

'''Just print the board'''
def printBoard(board):
    print("-------------")
    for i in range(0,3):
        print("| " + board[i][0] + " | "+ board[i][1] + " | "+ board[i][2] + " |")
        print("-------------")

playagain = "Y"
thisMove = 0
'''keep repeating the game till player asks to quit'''
while playagain.upper() == "Y":
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    whoseTurn = ""
    playerXMoves = []
    playerOMoves = []
    thisPlayerMoves = []
    altWhoseTurn = lambda whoseTurn:"X" if whoseTurn=="O" else "O"
    altWhoseTurnMoves = lambda whoseTurn:playerXMoves if whoseTurn=="O" else playerOMoves
    '''select the starting player'''
    while whoseTurn.upper() != "X" and whoseTurn.upper() != "O":
        whoseTurn = input("Does Player 1 want X or O?").upper()
        
    '''check if any victory moves are available for either player'''
    movesAreAvailable = True
    while movesAreAvailable:
        
        '''get the next move'''
        printBoard(board)
        thisMove = input(whoseTurn + "'s next move:")
        
        '''validate the move'''
        if checkValidMove(board,thisMove) == False:
            continue
        
        '''add the move to the board'''
        board[(int(thisMove)-1)//3][(int(thisMove)-1)%3] = whoseTurn
        
        '''store player's moves in a list'''
        if whoseTurn == "X":
            playerXMoves.append(int(thisMove))
            thisPlayerMoves = playerXMoves
        else:
            playerOMoves.append(int(thisMove))
            thisPlayerMoves = playerOMoves
            
        '''check if player has won'''
        if checkVictory(thisPlayerMoves,whoseTurn) == True:
            printBoard(board)
            print("Congratulations!!! Player {} has won!".format(whoseTurn))
            break
        
        '''cycle the turn'''
        if whoseTurn == "X":
            whoseTurn = "O"  
            thisPlayerMoves = playerOMoves
        else:
            whoseTurn = "X"
            thisPlayerMoves = playerXMoves
        movesAreAvailable = areMovesAvailable(board, whoseTurn, thisPlayerMoves) or areMovesAvailable(board, altWhoseTurn(whoseTurn), altWhoseTurnMoves(whoseTurn))
    if not movesAreAvailable:
        print("No more moves left!")
    
    playagain = input("Do you wish to play again? Enter Y or N:")

