#Tutorial thanks to Christian Thompson
#https://www.youtube.com/watch?v=9jw4ndKDpBE

# STAGE ONE:
# Creating main loop
# Print the board
# Creating your loop
# Getting user input
# Making sure user input is acceptable
# Putting user input on board

# STAGE TWO:
# Checking to see if the player has one

# STAGE THREE:
# Creating a second player (not computer)
# Check for second player win
# Check for a full board (TIE)

# STAGE FOUR:
#

import os
import time
import random

#Defines the board
board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "] #Represents the board values - First one is index 0 so we ignore it

#Note - Make a game over function that takes inputs, and will display either X wins, O wins or Tie

#Print the header
def printHeader():
    print("TIC-TAC-TOE!!!")

#Define the printBoard function
def printBoard():
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("   |   |   ")

def XInput():
    while True:
        choice = input("Please choose an empty space for X. ")
        try:
            choice = int(choice)
            if choice in range(1, 10): #If the number is between 1 and 9 (Remember index starts with 0, continue.
                if board[choice] == " ":
                    board[choice] = "X"
                    break
                else:
                    print("Sorry, that space is taken")
                    time.sleep(1)
            else:
                print("Please enter a number between 1 and 9")
        except ValueError: #If something fails (i.e if choice = int(choice) fails, then run the following and redo the while loop
            print("Please enter a number between 1 and 9")


def CheckForXWin():
    if (board[1] == "X" and board[2] == "X" and board[3] == "X") or \
        (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
        (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
        (board[1] == "X" and board[4] == "X" and board[7] == "X") or \
        (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
        (board[3] == "X" and board[6] == "X" and board[9] == "X") or \
        (board[1] == "X" and board[5] == "X" and board[9] == "X") or \
        (board[3] == "X" and board[5] == "X" and board[7] == "X"):
        XWin = True
        return XWin
    else:
        XWin = False
        return XWin

def OInput():
    while True:
        choice = input("Please choose an empty space for O. ")
        try:
            choice = int(choice)
            if choice in range(1, 10): #If the number is between 1 and 9 (Remember index starts with 0, continue.
                if board[choice] == " ":
                    board[choice] = "O"
                    break
                else:
                    print("Sorry, that space is taken")
                    time.sleep(1)
            else:
                print("Please enter a number between 1 and 9")
        except ValueError: #If something fails (i.e if choice = int(choice) fails, then run the following and redo the while loop
            print("Please enter a number between 1 and 9")

def CheckForOWin():
    if (board[1] == "O" and board[2] == "O" and board[3] == "O") or \
        (board[4] == "O" and board[5] == "O" and board[6] == "O") or \
        (board[7] == "O" and board[8] == "O" and board[9] == "O") or \
        (board[1] == "O" and board[4] == "O" and board[7] == "O") or \
        (board[2] == "O" and board[5] == "O" and board[8] == "O") or \
        (board[3] == "O" and board[6] == "O" and board[9] == "O") or \
        (board[1] == "O" and board[5] == "O" and board[9] == "O") or \
        (board[3] == "O" and board[5] == "O" and board[7] == "O"):
        OWin = True
        return OWin
    else:
        OWin = False
        return OWin

def CheckForTie():
    isFull = True
    for index in range(1, 10):
        if board[index] == " ":
            isFull = False
            break

    # If the board is full, end the game
    if isFull == True:
        Tie = True
        return Tie
    elif isFull == False:
        Tie = False
        return Tie

def GameOver(XWin, OWin, Tie):
    os.system("cls")
    printHeader()
    printBoard()
    if Tie == True:
        print("Tie!")
        EndGame = True
        return EndGame
    elif XWin == True:
        print("X Wins! Congratulations!")
        EndGame = True
        return EndGame
    elif OWin == True:
        print("O Wins! Congratulations!")
        EndGame = True
        return EndGame
    else:
        EndGame = False
        return EndGame

def playAgain():
    global board
    while True:
        answer = input("Do you want to play again? ")
        if answer[0].lower() == "y":
            board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            return True
        elif answer == "":
            print("You know you need to type something, right?")

        else:
            print("Goodbye")
            return False

def main():
    while True:
        os.system("cls")
        printHeader()
        printBoard()

        XInput() #Registers X's input into the game
        XWin = CheckForXWin() #Gives XWin a value of either True or False, depending on whether X won or not
        OWin = CheckForOWin() #Gives OWin a value of either True or False, depending on whether O won or not
        Tie = CheckForTie() #Gives Tie a value of either True or False, depending on whether the board is full or not
        EndGame = GameOver(XWin, OWin, Tie)
        if EndGame == True:
            answer = playAgain()
            if answer == True:
                main()
            elif answer == False:
                break

        OInput()
        XWin = CheckForXWin()  # Gives XWin a value of either True or False, depending on whether X won or not
        OWin = CheckForOWin()  # Gives OWin a value of either True or False, depending on whether O won or not
        Tie = CheckForTie()  # Gives Tie a value of either True or False, depending on whether the board is full or not
        EndGame = GameOver(XWin, OWin, Tie)
        if EndGame == True:
            answer = playAgain()
            if answer == True:
                main()
            elif answer == False:
                break


main()