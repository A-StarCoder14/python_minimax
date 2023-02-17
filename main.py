import math
import sys
import random

class Tic_Tac_Toe:
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

    def __init__(self, difficulty):
        self.gameboard = [
            ['','',''],
            ['','',''],
            ['', '', '']
        ]
        self.difficulty = difficulty

    def checkWinner(self):
        for i in range(len(self.gameboard)):
            for j in range(len(self.gameboard[0])):
                # check horizontal
                if self.gameboard[j][0] != " " and self.gameboard[j][0] == self.gameboard[j][1] and self.gameboard[j][0] == self.gameboard[j][2]:
                    return self.gameboard[j][0]

                # check vertical
                elif self.gameboard[0][j] != " " and self.gameboard[0][j] == self.gameboard[1][j] and self.gameboard[1][j] == self.gameboard[2][j]:
                    return self.gameboard[0][j]

                # check diagonal
                elif self.gameboard[0][0] != " " and self.gameboard[0][0] == self.gameboard[1][1] and self.gameboard[0][0] == self.gameboard[2][2]:
                    return self.gameboard[0][0]
                elif self.gameboard[0][2] != " " and self.gameboard[0][2] == self.gameboard[1][1] and self.gameboard[0][2] == self.gameboard[2][0]:
                    return self.gameboard[0][2]
        return "tie"

    def resetBoard(self):
         for i in range(len(self.gameboard)):
             for j in range(len(self.gameboard)):
                 self.gameboard[i][j] = " "

    def printBoard(self):
        print(f"""
          {self.gameboard[0][0]}  |  {self.gameboard[0][1]}  | {self.gameboard[0][2]}
         ----|-----|----
          {self.gameboard[1][0]}  |  {self.gameboard[1][1]}  | {self.gameboard[1][2]}
         ----|-----|----
          {self.gameboard[2][0]}  |  {self.gameboard[2][1]}  | {self.gameboard[2][2]}
         """)

    def checkFreeSpaces(self):
        freeSpaces = 9
        for i in self.gameboard:
            for j in i:
                if j != " ":
                    freeSpaces -= 1

        return freeSpaces

    def playerMove(self):
        row = 0
        column = 0
        while True:
            try:
                row = int(input("Select a row #: (1, 2, 3) "))
                column = int(input("Select a column #: (1,2,3) "))
                if row > 0 and row <= 3 and column > 0 and column <= 3 and self.gameboard[row-1][column-1] == " ":
                    break
                print("Enter a number between 1 - 3 and make sure the spot you pick is not already taken.")
            except ValueError:
                print("Please enter a number between 1 - 3.")
        self.gameboard[row-1][column - 1] = Tic_Tac_Toe.PLAYER

    def minimax(self, isMaximising):
        if self.checkWinner() == Tic_Tac_Toe.PLAYER:
            return -1
        elif self.checkWinner() == Tic_Tac_Toe.AI:
            return 1
        elif self.checkFreeSpaces() == 0:
            return 0

        if isMaximising:
            bestscore = -1000
            for i in range(len(self.gameboard)):
                for j in range(len(self.gameboard[0])):
                    if self.gameboard[i][j] == " ":
                        self.gameboard[i][j] = Tic_Tac_Toe.AI
                        score = self.minimax(False)
                        self.gameboard[i][j] = " "
                        if score > bestscore:
                            bestscore = score
            return bestscore
        else:
            bestscore = 1000
            for i in range(len(self.gameboard)):
                for j in range(len(self.gameboard[0])):
                    if self.gameboard[i][j] == " ":
                        self.gameboard[i][j] = Tic_Tac_Toe.PLAYER
                        score = self.minimax(True)
                        self.gameboard[i][j] = " "
                        if score < bestscore:
                            bestscore = score
            return bestscore

    def minimax_move(self):
        bestscore = -1000
        bestmove = (0, 0);
        for i in range(len(self.gameboard)):
            for j in range(len(self.gameboard[0])):
                if self.gameboard[i][j] == " ":
                    self.gameboard[i][j] = Tic_Tac_Toe.AI
                    score = self.minimax(False)
                    self.gameboard[i][j] = " "
                    if score > bestscore:
                        bestscore = score
                        bestmove = (i, j)
        self.gameboard[bestmove[0]][bestmove[1]] = Tic_Tac_Toe.AI
 
    def ai_random_move(self):
        while True:
            ai_row = random.randint(0,2)
            ai_column = random.randint(0,2)
            if self.gameboard[ai_row][ai_column] == " ":
                self.gameboard[ai_row][ai_column] = Tic_Tac_Toe.AI
                break

    def go_hard(self):
        if self.gameboard[2][2] == " ":
            self.gameboard[2][2] = Tic_Tac_Toe.AI
            self.printBoard()
        elif self.gameboard[2][0] == " ":
            self.gameboard[2][0] = Tic_Tac_Toe.AI
            self.printBoard()

    def startGame(self):
        self.resetBoard()
        print("-" * 30)
        print(" " * 8 + "Tic Tac Toe")
        print("-" * 30)
        if self.difficulty == 'HARD':
            self.gameboard[0][0] = Tic_Tac_Toe.AI
        else:
            self.ai_random_move()
        self.printBoard()
        self.playerMove()
    
    def start(self):
        self.startGame()
        # If difficulty 'MEDIUM' or 'HARD' is chosen
        if self.difficulty == "MEDIUM" or self.difficulty == "HARD":
            if self.difficulty == "HARD":
                self.go_hard()
                self.playerMove()
            while True:
                self.minimax_move()
                self.printBoard()
                if game.checkWinner() != 'tie' or game.checkFreeSpaces() == 0:
                    break
                self.playerMove()
                self.printBoard()
                if game.checkWinner() != 'tie' or game.checkFreeSpaces() == 0:
                    break
            if self.checkWinner() == Tic_Tac_Toe.PLAYER:
                print("You won")
            elif self.checkWinner() == Tic_Tac_Toe.AI:
                print("You lost")
            else:
                print("Its a tie")

        if self.difficulty == "EASY":
            while True:
                self.ai_random_move()
                self.printBoard()
                if game.checkWinner() != 'tie' or game.checkFreeSpaces() == 0:
                    break
                self.playerMove()
                self.printBoard()
                if game.checkWinner() != 'tie' or game.checkFreeSpaces() == 0:
                    break
            if self.checkWinner() == Tic_Tac_Toe.PLAYER:
                print("You won")
            elif self.checkWinner() == Tic_Tac_Toe.AI:
                print("You lost")
            else:
                print("Its a tie")


levels = ["EASY", "MEDIUM", "HARD"]
try:
    program, difficulty = sys.argv
    if not difficulty.upper() in levels:
        print("Please enter one of the following for the difficulty levels:\n\n\teasy | medium | hard")
        exit(1)
except ValueError:
    print("Please enter a difficulty level for the game:\n\n\teasy | medium | hard")
else:
    game = Tic_Tac_Toe(difficulty.upper())
    game.start()
