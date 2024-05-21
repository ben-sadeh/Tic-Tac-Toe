############################################################
# Name: Ben Sadeh
# Date: May 20, 2024
# Title: Question 1: Two Player Tic-Tac-Toe game
############################################################


##############################
# Classes
##############################
class TTT:
    def __init__(self, player1, player2):
        self.board= {'7': ' ' , '8': ' ' , '9': ' ' ,
                    '4': ' ' , '5': ' ' , '6': ' ' ,
                    '1': ' ' , '2': ' ' , '3': ' ' }
        self.player1=player1
        self.player2=player2
        self.count=0
        self.turn=player1

        self.board_keys = []
        for key in self.board:
            self.board_keys.append(key)
    
    # Print the board
    def printBoard(self):
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])
        print('-+-+-')
        print(self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'])
        print('-+-+-')
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'])
    
    # Main method with all the gameplay functionality
    def play(self):
        inPlay=True
        while inPlay:
            self.printBoard()
            print("It's your turn," + self.turn.name + ".Move to which place?")

            move = input()        

            if self.board[move] == ' ':
                self.board[move] = self.turn.symbol
                self.count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # Check if player has won 
            if self.count >= 5:
                if (self.board['7'] == self.board['8'] == self.board['9'] != ' ') or \
                (self.board['4'] == self.board['5'] == self.board['6'] != ' ') or \
                (self.board['1'] == self.board['2'] == self.board['3'] != ' ') or \
                (self.board['1'] == self.board['4'] == self.board['7'] != ' ') or \
                (self.board['2'] == self.board['5'] == self.board['8'] != ' ') or \
                (self.board['3'] == self.board['6'] == self.board['9'] != ' ') or \
                (self.board['7'] == self.board['5'] == self.board['3'] != ' ') or \
                (self.board['1'] == self.board['5'] == self.board['9'] != ' '):

                    self.printBoard()
                    print("\nGame Over.\n")                
                    print(" **** " +self.turn.name + " won. ****")                
                    inPlay=False

            # If neither player wins and the board is full the game in a tie
            if self.count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")
                inPlay=False

            # Change the player after each move
            if self.turn ==self.player1:
                self.turn = self.player2
            else:
                self.turn = self.player1

        # See if the players want to restart the game
        self.restart()

    #Restart the game    
    def restart(self):
        restart = input("Do want to play Again?(y/n)")
        if restart.lower() == "y":
            for key in self.board_keys:
                self.board[key] = " "
            self.count=0
            self
            self.play()

# Each player will have its own Player object associated with it
class Player:
    def __init__(self, name, symbol):
        self.name=name
        self.symbol=symbol
    def __str__(self):
        return self.name
    

##############################
# Main program
##############################
print("What is player 1s name?")
player1=Player(input(),'X')
print("What is player 2s name?")
player2=Player(input(),'O')
Game=TTT(player1, player2)
Game.play()
