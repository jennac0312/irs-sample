# This game plays Glass Bridge, inspired by the Glass Bridge scene from Squid Games
# Player will select the length of the bridge to play on (between 1 and 5)
# The catch is that one (random) side of the bridge has a false panel
# If the Player jumps to the false panel side, it's GAME OVER.
# If the Player manages to avoid all false panels, the Player wins!
# Player will enter a number between 1 and 5 to select the length of the bridge.
# Player will use letters 'l' and 'r' to select left and right path, respectively

#Importing the randint module
from random import randint
#Importing to differentiate progress more easily in console
from colorama import Back, Fore, Style


# purpose: prompt Player to input the number of jumps - jumps are the game length
def getBridgeLength():
  # get length from Player input
  bridgeLength = input(Fore.LIGHTBLUE_EX +
                       "How many jumps would you like to attempt? " +
                       Style.RESET_ALL)
  # check if input is a number between 1-5

  while bridgeLength not in [ f"{num}" for num in range(1,21)]:
    bridgeLength = input(Fore.BLUE +
                        #  "Please enter a number between 1 and 5: " +
                         "Please enter a number between 1 and 20: " +
                         Style.RESET_ALL)
  # announce bridge length
  print(Back.YELLOW +
        f"You must complete {bridgeLength} jump(s) successfully to win." +
        Style.RESET_ALL)
  return int(bridgeLength)  # return as number

# purpose: to determine the success probability based on chosen bridge length.
def showSuccessProbability(bridgeLength):
  # calculate percentage
  probability = ((1 / 2)**bridgeLength) * 100
  # display probability
  print(Fore.RED + 'You have a ' + str(probability) + '% chance of success' +
        Style.RESET_ALL)

# purpose: prompt Player to choose a path (left or right)
def getPlayerJump():
  # get player input for which path they want to take
  # l = left(0), r = right(1)
  playJump = input(Fore.LIGHTBLUE_EX +
                   "Which path would you like to take? (l or r): " +
                   Style.RESET_ALL)
  # check if input is l or r
  while playJump.lower() not in ['l', 'r']:
    playJump = input(Fore.BLUE + "Please enter l or r: " + Style.RESET_ALL)
  # assign path based on input
  path = ('LEFT' if playJump.lower() == 'l' else 'RIGHT')
  # display path chosen
  print('You have chosen to jump ' + path + '. Good Luck!')
  return path

# purpose: generates a random success path for the bridge.
def generateSuccessPath(bridgeLength):
  successPath = []
  # loop to get array = bridgeLength
  for _ in range(int(bridgeLength)):
    successPath.append(randint(0, 1))  # take random number, add to array
  print('SUCCESS PATH: ', successPath)  # uncomment to cheat and show success path
  return successPath

# purpose: generate a single row of the bridge based on player's progress.
def getOneBridgeRow(playerPath, round):
  # if player has not reached the round yet, print an empty path
  if round >= len(playerPath):
    return '_ _'
  # if player is at or beyond the current round and jumped left
  elif playerPath[round] == 0:
    return '* _'
  # if player is at or beyond the current round and jumped right
  else:
    return '_ *'

# purpose: display entire bridge with the player's progress up to current round
def displayBridge(bridgeLength, playerPath, round):
  # bridge length = rows
  rows = int(bridgeLength)

  print(Back.WHITE + Fore.BLACK + "START" + Style.RESET_ALL)
  # loop and print each bridge row separately
  for i in range(rows):
    # if round is 0 print empty complete bridge
    if round == 0:
      print('_ _')
    # else print bridge with player path up to current round
    else:
      # print current bridge row
      print(getOneBridgeRow(playerPath, i))
  print()  # add space
  print(Back.WHITE + Fore.BLACK + "FINISH" + Style.RESET_ALL)
  print()  # add space

# purpose: tracks the player's chosen path for each jump
def trackPlayerPath(path, playerPath):
  # convert path(l/r) to 0/1
  path = 0 if path == "LEFT" else 1
  # add jump to player path array
  playerPath.append(path)
  return playerPath

# purpose: checks if player's jump matches the successful path
def checkJump(playerPath, successPath, round):
  # check if player jumps on safe panel (true/false)
  return playerPath[round] == successPath[round]

# purpose: asks Player if they want to see the successful path
# displays solution if requested
def showSuccessPath(bridgeLength, successPath, round):
  showpath = input(Fore.LIGHTBLUE_EX +
                   "Would you like to see the successful path? (y or n): " +
                   Style.RESET_ALL)
  # check input
  while showpath.lower() not in ['y', 'n']:
    showpath = input(Fore.BLUE + "Please enter (y or n): " +
                     Style.RESET_ALL)  #blue text
  # if yes show success path
  if showpath.lower() == 'y':
    print()  # add space
    print(Fore.LIGHTGREEN_EX + "Successful Path:" + Style.RESET_ALL)
    displayBridge(bridgeLength, successPath, round)

# purpose: gameplay loop and control the flow of the game
# prompt player, track progress, check jumps, end game
def main():
  # initialize variables
  round = 0  # start of game
  playerPath = []  # track player progress

  # welcome message
  print(Fore.LIGHTMAGENTA_EX + "Welcome To Glass Bridge" + Style.RESET_ALL)
  print()  # add space

  # get bridge length from Player
  bridgeLength = getBridgeLength()
  # show success probability
  showSuccessProbability(bridgeLength)
  # get success path
  successPath = generateSuccessPath(bridgeLength)
  # display starting bridge
  displayBridge(
      bridgeLength, False,
      round)  # false because no playerPath yet.. Player didnt take a turn yet

  # loop until player fails a jump
  while True:
    # get Player jump
    playerJump = getPlayerJump()
    # track player path
    playerPath = trackPlayerPath(playerJump, playerPath)
    # check player jump success/fail
    successfulJump = checkJump(playerPath, successPath, round)
    # if jump fail
    if not successfulJump:
      # incremnet round
      round += 1
      print(Fore.RED + "Sorry you chose the wrong path!" +
            Style.RESET_ALL)
      # ask to show success path
      showSuccessPath(bridgeLength, successPath, round)

      print()  # add space
      print('Better luck next time.')
      break  # end loop if player fails jump
    # if jump success
    else:
      print()
      print(Fore.LIGHTGREEN_EX + "Nice Work" + Style.RESET_ALL)

      round += 1  # increment round

      # check if game complete
      if round <= bridgeLength:  # <= displays final jump
        # if rounds remaining announce next round
        if bridgeLength - round > 0:
          print()
          print('Next Round')
        # display updated bridge
        displayBridge(bridgeLength, playerPath, round)
      # if Player made it to end of bridge congrats. end game
      if round == bridgeLength:
        print(Fore.LIGHTYELLOW_EX +
              'CONGRATULATIONS! You conquered the Glass Bridge' +
              Style.RESET_ALL)
        break  # end loop

  # ask to play again
  playAgain = input(Fore.LIGHTBLUE_EX +
                    "Would you like to play again? (y or n) " +
                    Style.RESET_ALL)
  while playAgain.lower() not in ['y', 'n']:
    playAgain = input(Fore.BLUE + "Please enter (y or n): " + Style.RESET_ALL)
  if playAgain.lower() == 'y':
    print()  # add space
    print()  # add space
    main()  # play game again
  else:
    print()  # add space
    print(Fore.RED + "Goodbye, Player")

main()
