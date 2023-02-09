import math
import random

winningcombo = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

PLAYER = "X"
AI = "O"

gameboard = [
    ['','',''],
    ['','',''],
    ['', '', '']
]

def checkWinner():
    for i in range(len(gameboard)):
        for j in range(len(gameboard[0])):
            # check horizontal
            if gameboard[j][0] != " " and gameboard[j][0] == gameboard[j][1] and gameboard[j][0] == gameboard[j][2]:
                return gameboard[j][0]

            # check vertical
            elif gameboard[0][j] != " " and gameboard[0][j] == gameboard[1][j] and gameboard[1][j] == gameboard[2][j]:
                return gameboard[0][j]

            # check diagonal
            elif gameboard[0][0] != " " and gameboard[0][0] == gameboard[1][1] and gameboard[0][0] == gameboard[2][2]:
                return gameboard[0][0]
            elif gameboard[0][2] != " " and gameboard[0][2] == gameboard[1][1] and gameboard[0][2] == gameboard[2][0]:
                return gameboard[0][2]
    return "tie"

def resetBoard():
     for i in range(len(gameboard)):
         for j in range(len(gameboard)):
             gameboard[i][j] = " "


def printBoard():
    print(f"""
      {gameboard[0][0]}  |  {gameboard[0][1]}  | {gameboard[0][2]}
     ----|-----|----
      {gameboard[1][0]}  |  {gameboard[1][1]}  | {gameboard[1][2]}
     ----|-----|----
      {gameboard[2][0]}  |  {gameboard[2][1]}  | {gameboard[2][2]}
     """)

def checkFreeSpaces():
    freeSpaces = 9
    for i in gameboard:
        for j in i:
            if j != " ":
                freeSpaces -= 1

    return freeSpaces


def startGame():
    resetBoard()
    print("-" * 30)
    print(" " * 8 + "Tic Tac Toe")
    print("-" * 30)


def playerMove():
    row = 0
    column = 0
    while row < 1 or row > 3:
            row = int(input("Select a row #: (1, 2, 3) "))
    while column < 1 or column > 3:
            column = int(input("Select a column #: (1,2,3) "))
    while gameboard[row -1][column-1] != " ":
        row = int(input("Select a row #: (1, 2, 3) "))
        column = int(input("Select a column #: (1,2,3) "))
    gameboard[row-1][column - 1] = PLAYER

def minimax(board, depth, isMaximising):
    if checkWinner() == PLAYER:
        return -1
    elif checkWinner() == AI:
        return 1
    elif checkFreeSpaces() == 0:
        return 0


    if isMaximising:
        bestscore = -1000
        for i in range(len(gameboard)):
            for j in range(len(gameboard[0])):
                if gameboard[i][j] == " ":
                    gameboard[i][j] = AI
                    score = minimax(gameboard, 0, False)
                    gameboard[i][j] = " "
                    if score > bestscore:
                        bestscore = score
        return bestscore
    else:
        bestscore = 1000
        for i in range(len(gameboard)):
            for j in range(len(gameboard[0])):
                if gameboard[i][j] == " ":
                    gameboard[i][j] = PLAYER
                    score = minimax(gameboard, 0, True)
                    gameboard[i][j] = " "
                    if score < bestscore:
                        bestscore = score
        return bestscore


def starting_rounds():
    gameboard[0][0] = AI
    printBoard()
    playerMove()


def main():

    ai_row = math.floor((random.random()*1000) %3)+1
    ai_column = math.floor((random.random()*1000 %3))+1

    startGame()
    starting_rounds()
    while True:
        bestscore = -1000
        bestmove = (0, 0);
        for i in range(len(gameboard)):
            for j in range(len(gameboard[0])):
                if gameboard[i][j] == " ":
                    gameboard[i][j] = AI
                    score = minimax(gameboard, 0, False)
                    gameboard[i][j] = " "
                    if score > bestscore:
                        bestscore = score
                        bestmove = (i, j)
        gameboard[bestmove[0]][bestmove[1]] = AI
        if checkWinner() != 'tie' or checkFreeSpaces() == 0:
            break
        printBoard()
        playerMove()
        if checkWinner() != 'tie' or checkFreeSpaces() == 0:
            break

    printBoard()
    if checkWinner() == PLAYER:
        print("You won")
    elif checkWinner() == AI:
        print("You lost")
    else:
        print("Its a tie")

main()