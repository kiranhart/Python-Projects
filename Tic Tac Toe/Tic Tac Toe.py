'''
                        TIC TAC TOE
This is a Console Tic Tac Toe Game made by Kiran Hart.
'''

import time
import random

PLAYER_ONE_CHARACTER = " X "
PLAYER_TWO_CHARACTER = " O "
PLAYER_BLANK = "   "

chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
         "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "=", "<", "?", ">", "/"]

board = ["   ", "   ", "   ", 
       "   ", "   ", "   ",
       "   ", "   ", "   "]
       
playerOneTurn = True
twoPlayers = True

gameSetup = False
playerOneSetup = False
playerTwoSetup = False

#Method to display the credits
def gameCredits():
  print("-----------------------------------")
  print("            TIC TAC TOE")
  print("-----------------------------------")
  print("")
  print("Created By Kiran Hart - Version 2.0")
  print("")
  print("-----------------------------------")
  print("")
  print("")
  print("")

def getRandomCharacter(): 
    return chars[random.randint(0, len(chars) - 1)]
  
def drawBoard(): 
  print("-----------------")
  print("|" + board[0] + " | " + board[1] + " | " + board[2] + "|")
  print("-----------------")
  print("|" + board[3] + " | " + board[4] + " | " + board[5] + "|")
  print("-----------------")
  print("|" + board[6] + " | " + board[7] + " | " + board[8] + "|")
  print("-----------------")

def clearScreen():
  x = 0
  while(x < 30):
    print("  ")
    x += 1

def clearBoard():
  for index in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
      board[index] = PLAYER_BLANK

def checkWinner(player): 
  won = False
  if(board[0] == player and board[1] == player and board[2] == player): 
    won = True
  elif(board[3] == player and board[4] == player and board[5] == player): 
    won = True
  elif(board[6] == player and board[7] == player and board[8] == player): 
    won = True
  elif(board[0] == player and board[4] == player and board[8] == player): 
    won = True
  elif(board[2] == player and board[4] == player and board[6] == player): 
    won = True
  return won
    
def isTie(): 
    tie = False
    if(board[0] != PLAYER_BLANK and board[1] != PLAYER_BLANK and board[2] != PLAYER_BLANK and board[3] != PLAYER_BLANK and board[4] != PLAYER_BLANK 
    and board[5] != PLAYER_BLANK and board[6] != PLAYER_BLANK and board[7] != PLAYER_BLANK and board[8] != PLAYER_BLANK): 
        tie = True
    return tie
    
def updateBoard(character, slot): 
    board[slot - 1] = character

    
while True: 

  if(checkWinner(PLAYER_ONE_CHARACTER) or checkWinner(PLAYER_TWO_CHARACTER) or isTie()):

    print("")
    print("")
    drawBoard()
    print("")
    print("")
    if(checkWinner(PLAYER_ONE_CHARACTER)):
        print("Congrats, Player:", PLAYER_ONE_CHARACTER, "has won")
        print("Setting up the new game!")
    elif(checkWinner(PLAYER_TWO_CHARACTER)):
        print("Congrats, Player:", PLAYER_TWO_CHARACTER, "has won")
        print("Setting up the new game!")
    elif(isTie()):
        print("There are no winners, better luck next time.")
        print("Setting up the new game!")
    print("")
    print("")

    gameSetup = False
    playerOneSetup = False
    playerTwoSetup = False
    time.sleep(3)
    clearScreen()
  
  if(not(gameSetup)):
    gameCredits()
    print("")
    print("Looks like it's a new game!, Let's setup some basic information.")
    print("")
    print("")
    validGameMode = False
    while(not(validGameMode)):
        usingSinglePlayer = input("Are you playing Solo? (y/n): ")
        if(usingSinglePlayer == "y"): 
            twoPlayers = False
            validGameMode = True
        elif(usingSinglePlayer == "n"): 
            twoPlayers = True
            validGameMode = True
    print("")
    print("")
    while(not(playerOneSetup)): 
        print("Player 1, Please enter a character (Default is X): ")
        PLAYER_ONE_CHARACTER = input()
        if (len(PLAYER_ONE_CHARACTER) == 1):
            PLAYER_ONE_CHARACTER = " " + PLAYER_ONE_CHARACTER + " "
            playerOneSetup = True
        else: 
            print("Error: Please use a single letter or character!")
    while(not(playerTwoSetup)): 
        if(twoPlayers): 
            print("Player 2, Please enter a character (Default is O): ")
            PLAYER_TWO_CHARACTER = input()
            if (len(PLAYER_TWO_CHARACTER) == 1):
                PLAYER_TWO_CHARACTER = " " + PLAYER_TWO_CHARACTER + " "
                playerTwoSetup = True
            else: 
                print("Error: Please use a single letter or character!")
        else: 
            print("Computer is picking their symbol...")
            validAIChar = False
            while(not(validAIChar)): 
                selectedChar = " " + random.choice(chars) + " "
                if (selectedChar != PLAYER_ONE_CHARACTER): 
                    PLAYER_TWO_CHARACTER = selectedChar
                    validAIChar = True
                    playerTwoSetup = True

    print("")
    print("Look's like everything is good to go.")
    print("")
    print("Player 1 Symbol: ", PLAYER_ONE_CHARACTER)
    print("Player 2 Symbol: ", PLAYER_TWO_CHARACTER)
    clearBoard()
    gameSetup = True
    
  #End of Game Setup
  drawBoard()

  slotValid = False
  selectedSlot = None;

  while(selectedSlot is not int):
      try:
          print("")
          if(playerOneTurn): 
              print("(Player:", PLAYER_ONE_CHARACTER, ")", "Please enter a valid slot (1-9)")
          else: 
              if(twoPlayers):
                  print("(Player:", PLAYER_TWO_CHARACTER, ")", "Please enter a valid slot (1-9)")
          print("")
          if (not(twoPlayers) and not(playerOneTurn)): 
              aiPass = False
              while(not(aiPass)): 
                  aiSlot = random.randint(0, 8)
                  if(board[aiSlot] == PLAYER_BLANK): 
                      aiPass = True
                      selectedSlot = aiSlot
          else: 
              selectedSlot = int(input())
          break
      except ValueError:
          print("")
          print("Error: Enter a number between 1 - 9")
          print("")

  if (selectedSlot >= 1 and selectedSlot <= 9):
    if (board[selectedSlot - 1] != PLAYER_BLANK):
        print("")
        print("Sorry, but that slot has already been taken!")
        print("")
        slotValid = False
    else:
       if (playerOneTurn):
          updateBoard(PLAYER_ONE_CHARACTER, selectedSlot)
          playerOneTurn = False
          slotValid = False
       else:
          updateBoard(PLAYER_TWO_CHARACTER, selectedSlot)
          playerOneTurn = True
          slotValid = False
