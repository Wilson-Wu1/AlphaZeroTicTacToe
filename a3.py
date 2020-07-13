#a3.py
#Wilson Wu
#301350197

# -----------------------------------------------------------------------------------------------------------------------------------
# Pure MCTS is a greedy algorithm, choosing the optimal solution at a given state. 
#
# Due to the random nature of random playouts, a 100% guranatee of winning is not possible without other game logic.
# The issue with pure MCTS on a tic tac toe game is the program cannot account for a state which is unwinnable.
#
# A state is unwinnable if the player has two options to win with one move. The robot can only block one option.
# When the robot encounters such state during its playouts, the robot will not determine or compensate for the unwinnalbe state.
#
# Due to the restrictions of our assignment (pure MCTS), there is 1 case where the player can win (given the player goes first).
#
# In my testings, I have the player go first because this gives a big disadvantage to the robot.
# However, the user can pick who gets to go first.
# -----------------------------------------------------------------------------------------------------------------------------------
# Case 1) 
# 1. The player places a x on any corner. The robot will place an o in the center.
# 2. The player places an x in the opposite corner of the first x. 
# 3. If the robot places the next o in any 2 corners, the robot has lost.
# 4. The player will place an x in the last remaining corner to create an unwinnable state for the robot.

#
# o |   | x                 o |   | x    
# ---------  Player Goes    ---------
#   | o |       --->          | o |  
# ---------                 ---------
# x |   |                   x |   | x
# 
# This unwinnable state is preventable by having the robot place an o in a non-corner tile during its first turn by changing wieghts. 
# But the change of weights have led to other unwinnable states.

# -------------------
# number of playouts = 1000
# playerWin = -2
# robotWin = +2
# Draw = +1
# x = player
# o = robot
# -------------------
# I chose 1000 to be my number of playouts because the only case where it loses is the Case 1 shown below.
# Playouts less than 1000 have also resulted in DIFFERENT unwinnable states.
# More playouts creates a more even distribution to the possible playout states.
#
# Player and Robot to having the same weight was a good heurisitic for my program. 
# Draw was set to 2 because we want the program to at least draw (never lose).

import random

# Displays all legal moves to user.
def displayMoves(legalMoves):
    moveList = legalMoves
    
    print("POSSIBLE MOVES")
   
    print(moveList[0],'|',moveList[1],'|',moveList[2])
    print("---------")
    print(moveList[3],'|',moveList[4],'|',moveList[5])
    print("---------")
    print(moveList[6],'|',moveList[7],'|',moveList[8])
    print('\n')

# Displays the current board state to user.
def displayBoard(board):
    tempBoard = board.copy()
    print("--BOARD--")

    for i in range(9):
        if(tempBoard[i] == 1):
            tempBoard[i] = 'x'
        elif(tempBoard[i]==2):
            tempBoard[i] = 'o'
        else:
            tempBoard[i] = ' '

    
    print(tempBoard[0],'|',tempBoard[1],'|',tempBoard[2])
    print("---------")
    print(tempBoard[3],'|',tempBoard[4],'|',tempBoard[5])
    print("---------")
    print(tempBoard[6],'|',tempBoard[7],'|',tempBoard[8])
    print('\n')



    

    
# Used to check if the PLAYER has won by checking all possible winning positions
def checkMatePlayer(board):
    #ROWS
    if(board[0]==1 and board[1]==1 and board[2]==1):
        
        return True
    if(board[3]==1 and board[4]==1 and board[5]==1):
        
        return True
    if(board[6]==1 and board[7]==1 and board[8]==1):
        
        return True
    #COLUMNS
    if(board[0]==1 and board[3]==1 and board[6]==1):
        
        return True
    if(board[1]==1 and board[4]==1 and board[7]==1):
        
        return True
    if(board[2]==1 and board[5]==1 and board[8]==1):
        
        return True
    #DIAG
    if(board[0]==1 and board[4]==1 and board[8]==1):
        
        return True
    if(board[2]==1 and board[4]==1 and board[6]==1):
        
        return True

# Used to check if the ROBOT has won by checking all possible winning positions
def checkMateBot(board):
    #ROWS
    if(board[0]==2 and board[1]==2 and board[2]==2):

        return True
    if(board[3]==2 and board[4]==2 and board[5]==2):
        
        return True
    if(board[6]==2 and board[7]==2 and board[8]==2):
        
        return True
    #COLUMNS
    if(board[0]==2 and board[3]==2 and board[6]==2):
        
        return True
    if(board[1]==2 and board[4]==2and board[7]==2):
        
        return True
    if(board[2]==2 and board[5]==2 and board[8]==2):
        
        return True
    #DIAG
    if(board[0]==2 and board[4]==2 and board[8]==2):
        
        return True
    if(board[2]==2 and board[4]==2 and board[6]==2):
        
        return True

# Returns the number of open tiles
def numberOfOpenTiles(board):
    counter = 0
    for i in board:
        if i == 0:
            counter +=1
    return counter

# Function returns the TILE NUMBER with the greatest number of wins from resultList.
def getMaxTile(resultList,legalMoves):
    max = -99999999999999999999
    

    for i in range(len(resultList)):
        if legalMoves[i] != ' ':        # Must be a legal move first of all
            if resultList[i] > max:
                max = resultList[i]               
                result = i
    return result

     
           
# AlphaZero function used to play "numOfPlayout" of random playouts.
def alphaZero(board,legalMoves,display = False):
    #Intialize Variables
    numOfPlayout = 1000            # ***HEURISTIC: number of playouts 
    initialBoard = board.copy()             # Copy the initial board
    playerWins = 0      
    botWins = 0
    draw = 0
    open =  numberOfOpenTiles(board)
    resultList = [0,0,0,0,0,0,0,0,0]        # Results from random playouts              
    #print("AlphaZero Calcuating . . .")
    
    #Loop through every avaliable tile on board
    for i in range(len(board)):
        #Loop through the number of playouts
        for j in range(numOfPlayout):
            #INITIALIZING NEW BOARD
            board = initialBoard.copy()
            if(display == True):
                print("-------------------------------------------")
                print("ITERATION:",j+1,"  TILE:", i)
                print('\n')           
                print("CURRENT STATS")
                print("-------------")
                print("Player Wins:" ,playerWins)
                print("Bot Wins:", botWins)
                print("Draws:", draw)
                print("-------------------------------------------")
            win = False
            open =  numberOfOpenTiles(board)
        
            #BOT INITIAL MOVE
            if board[i] == 0:
                board[i] = 2
                #displayMoves(board)
                if(checkMateBot(board) == True):
                    botWins+=1
                    #print(botWins,"BotWins")
                    win = True

                    # I use +numOfPlayout for the heuristic for the INITIAL/FIRST ROBOT MOVE.
                    # This tells the algorithm that if it can win in ONE move, then play that move.
                    # If this was instead +1 or +2, then the algorithm may or may not choose this as the next move.
                    # It would also result in a loss or prolong the game using +1 or +2.
                    # This should always be more than the number of Playouts.
                    resultList[i]+=numOfPlayout # ***HEURISTIC: FIRST ROBOT MOVE RESULTS IN A WIN

                #BEGIN RANDOM MOVES BETWEEN PLAYER AND BOT
                numberOfPlayerMoves = -1
                while win == False:
                    numberOfPlayerMoves +=1
                    
                    
                    #Player Move
                    open =  numberOfOpenTiles(board)
                    if(open!=0):
                        validSpot = False
                        while validSpot == False:
                            testInt = random.randint(0,8)
                            if board[testInt]==0:
                                board[testInt]=1
                                validSpot = True                               
                        
                        #Check for Player Win Condition
                        if(checkMatePlayer(board) == True):
                            #Results when the player will win in one move.
                            if(numberOfPlayerMoves == 0):
                                resultList[testInt] = resultList[testInt] + (numOfPlayout/2)    
                            else:                     
                                resultList[i]-= 2       # ***HEURISTIC: HOW MUCH IS A LOSS WORTH?
                            playerWins +=1
                            break
          
                    
                    #Bot Move
                    open =  numberOfOpenTiles(board)
                    if(open!=0):
                        validSpot = False
                        while validSpot == False:
                            testInt = random.randint(0,8)
                            if board[testInt]==0:
                                board[testInt]=2
                                validSpot = True
                                open -=1       
                        #Check for Bot Win Condition
                        if(checkMateBot(board) == True):
                            botWins+=1                         
                            resultList[i]+=2           # ***HEURISTIC: HOW MUCH IS A WIN WORTH?
                            break

                    #Draw, neither bot or player wins.
                    if(win == False and open == 0):
                        draw += 1
                        resultList[i]+=2                 # ***HEURISTIC: HOW MUCH IS A DRAW WORTH?
                        win = True

    #Play Best Tile

    board = initialBoard.copy()
    checkIfDraw = False
    #Check if every tile on the board is used
    for i in range(len(resultList)):
        if resultList[i]!=0:
            checkIfDraw = True
            break
    #If resultList returns all 0s, then the first legal move is choosen
    if(checkIfDraw == False):
        bestTile = playFirstAvaliableChoice(board)
        board[bestTile] = 2
        legalMoves[bestTile] = ' ' 
    #Pick Best Tile from resultList
    else:
        bestTile = getMaxTile(resultList,legalMoves)
        board[bestTile] = 2
        legalMoves[bestTile] = ' '


    #PRINT FINAL RESULTS OF TOTAL WINS, BEST TILE, AND RESULTING HEURISTIC LIST       

    #print("TOTAL Player Wins:" ,playerWins)
    #print("TOTAL Bot Wins:", botWins)          
    #print("TOTAL Draws:", draw)
    #print("Best Tile to play:",bestTile, "with a score of:",max(resultList))
    #print("Resulting Heuristic List:", resultList)
    #print('\n')
    return board
    

            
        

    


# Robot gets to play first
def botGoesFirst():
    #Initialize Empty Board
    gameOver = False
    legalMoves = [0,1,2,3,4,5,6,7,8]
    board = [0,0,0,0,0,0,0,0,0]
    #START GAME
    while gameOver!=True:
        inputChecker = False
        #AlphaZero Calculates and plays
        print("-------------------------------------------")
        board = alphaZero(board,legalMoves)        
        displayBoard(board)
        print("ALPHAZERO PLAYED")
        print('\n')
        #Check if Robot won / Draw
        if(checkMateBot(board) == True):
            print("GAMEOVER, ROBOT WINS!!!")
            print("-------------------------------------------")
            break

        if(numberOfOpenTiles(board) == 0):
            print("DRAW, NO MORE TILES LEFT")
            print("-------------------------------------------")
            gameOver = True
            inputChecker = True
        
        
        #Player Turn
        while inputChecker == False:
            displayMoves(legalMoves)
            PInput =input("Please enter your tile number:")
            PInput = int(PInput)
            #Invalid input
            if(PInput > 8) or (PInput < 0):
                print("ERROR: INVALID TILE NUMBER. PLEASE PICK A VALID TILE NUMBER")
            elif(legalMoves[PInput] == ' '):
                print("ERROR: TILE ALREADY FULL. PLEASE PICK A VALID TILE NUMBER")
            #Valid Input
            else:
                inputChecker = True
                legalMoves[PInput] = ' '
                board[PInput] = 1
                print("YOU PLAYED!")
                displayBoard(board)
                print("-------------------------------------------")
                #Check if Player won / Draw
                if(checkMatePlayer(board) == True):           
                    print("GAMEOVER, PLAYER WINS!!!")
                    print("-------------------------------------------")
                    gameOver = True

                elif(numberOfOpenTiles(board) == 0):
                    print("DRAW, NO MORE TILES LEFT")
                    print("-------------------------------------------")
                    gameOver = True




# Player gets to play first
def playerGoesFirst():
    #Initialize Board
    gameOver = False
    legalMoves = [0,1,2,3,4,5,6,7,8]
    board = [0,0,0,0,0,0,0,0,0]
    #START GAME
    while gameOver!=True:
        inputChecker = False
        #Player Goes
        print("-------------------------------------------")
        displayMoves(legalMoves)
        while inputChecker == False:   
            PInput =input("Please enter your tile number:")
            PInput = int(PInput)
            #Invalid Player Input
            if(PInput > 8) or (PInput < 0):
                print("ERROR: INVALID TILE NUMBER. PLEASE PICK A VALID TILE NUMBER")
            elif(legalMoves[PInput] == ' '):
                print("ERROR: TILE ALREADY FULL. PLEASE PICK A VALID TILE NUMBER")
            #Valid Player Input
            else:
                inputChecker = True

        legalMoves[PInput] = ' '
        board[PInput] = 1
        print("YOU PLAYED!")
        displayBoard(board)
        #Check if Player won / Draw
        if(checkMatePlayer(board) == True):
             
            print("GAMEOVER, PLAYER WINS!!!")
            print("-------------------------------------------")
            gameOver = True
            break
        elif(numberOfOpenTiles(board) == 0):
            print("DRAW, NO MORE TILES LEFT")
            print("-------------------------------------------")
            gameOver = True
            break
        #ROBOT Plays
        board = alphaZero(board,legalMoves)
        print("ALPHAZERO PLAYS")
        print('\n')
        displayBoard(board)
        print("-------------------------------------------")
        #Check if Robot won / Draw
        if(checkMateBot(board) == True):
            print("GAMEOVER, ROBOT WINS!!!")
            print("-------------------------------------------")
            break

        if(numberOfOpenTiles(board) == 0):
            print("DRAW, NO MORE TILES LEFT")
            print("-------------------------------------------")
            gameOver = True

# Randomly play until the player wins. Used for testing a set of weights a lot of times.
# *NOTE* The PLAYER ALWAYS goes first in this function because it makes it harder for the robot.
def testing():
    gamesPlayed = -1
    playerWon = False
    while playerWon == False:
        gamesPlayed +=1
        print("gamesPlayed:",gamesPlayed)
        gameOver = False
        legalMoves = [0,1,2,3,4,5,6,7,8]
        board = [0,0,0,0,0,0,0,0,0]
        #START GAME
        while gameOver!=True:
            validSpot = False
            #Player Goes
            print("-------------------------------------------")
            displayMoves(legalMoves)
            while validSpot == False:
                testInt = random.randint(0,8)
                if board[testInt]==0:
                    board[testInt]=1
                    legalMoves[testInt] = ' '
                    validSpot = True     

            print("YOU PLAYED!")
            displayBoard(board)
            #Check if Player won / Draw
            if(checkMatePlayer(board) == True):
             
                print("GAMEOVER, PLAYER WINS!!!")
                print("-------------------------------------------")
                gameOver = True
                playerWon = True
                break
            elif(numberOfOpenTiles(board) == 0):
                print("DRAW, NO MORE TILES LEFT")
                print("-------------------------------------------")
                gameOver = True
                break
            #ROBOT Plays
            board = alphaZero(board,legalMoves)
            print("ALPHAZERO PLAYS")
            print('\n')
            displayBoard(board)
            print("-------------------------------------------")
            #Check if Robot won / Draw
            if(checkMateBot(board) == True):
                print("GAMEOVER, ROBOT WINS!!!")
                print("-------------------------------------------")
                break

            if(numberOfOpenTiles(board) == 0):
                print("DRAW, NO MORE TILES LEFT")
                print("-------------------------------------------")
                gameOver = True
    
# Main function. Starts the program and asks who gets to go first.           
def gameMain():
    
        print("PROGRAM STARTED")
        print("-----------------")
        print('\n')
        validInput = False
        while validInput == False: 
            PInput = input("Who should go first? Enter 'x' for PLAYER or 'o' for ROBOT.")
            if PInput != 'o' and PInput != 'x':
                print("INVALID INPUT: Please Try Again.")
            elif(PInput == 'x'):
                print('\n')
                print("Player is playing first!")
                print('\n')
                playerGoesFirst()
                validInput = True
            else:
                print('\n')
                print("Robot is playing first!")
                print('\n')
                botGoesFirst()
                validInput = True


              
#playerGoesFirst()
#botGoesFirst()
#gameMain()
#testing()

if __name__ == '__main__':
  gameMain()