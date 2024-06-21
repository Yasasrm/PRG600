"""
Firstname: Yasas
Lastname: Maddumage
Username: YasasMaddumage
StudentID: 170308233
Email: yrmaddumage@myseneca.ca
"""

import sys
from random import randint

# 1 Marks
def rolldice():
    """
    function: rolldice prints two random numbers between 1 and 6 simulate two dices rolling. 
    The function should also print output of the numbers generated (Eg: 6 and 6) 
    return: int:total (total of two random numbers) 
    """
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    print(f"{dice1} and {dice2}")
    return dice1 + dice2

# 1 Marks 
def getplayers(): 
    """
    function:This functions asks user to provide an input of number of players. 
    Based on the number of players asks player names and create a list of player names and return player names
    If user entered invalid input for number of players (eg: string (a)) it throws an error and asks to retry 
    :return list:players (list of playernames entered by user)
    """
    while True:
        try:
            playerCount = int(input("Enter the number of players: "))
            if playerCount < 1:
                print("Please enter a valid number of players (1 or more).")
                continue
            players = []
            for i in range(playerCount):
                playerName = input(f"Enter name for player {i + 1}: ")
                players.append(newPlayer(players, playerName))
            return players
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def newPlayer(players, playerName):
    sameNameCount = 0
    for player in players:
        if player.lower() == playerName.lower():
            sameNameCount += 1
    return playerName if sameNameCount == 0 else f"{playerName}#{sameNameCount}"

# 1 Marks 
def getrounds(): 
    """
    function: This function asks user to enter the number of rounds they going to play 
    Based on the number of rounds entered as long it is valid return the number of rounds otherwise keep asking until a valid number entered. 
    :return int:roundcount (number of rounds)
    """
    while True:
        try:
            roundCount = int(input("Enter the number of rounds: "))
            if roundCount < 1:
                print("Please enter a valid number of rounds (1 or more).")
                continue
            return roundCount
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# 4 Marks 
def setgame():
    """
    function: This functions use the getplayers() function and getrounds() function to get player list and round count
    Using the above values setup a two dimensional (2D) list called game. The game list will have lists elements for each round and player 
    Eg: [[score1_1, score1_2, score1_3], [score2_1, score2_2, score2_3], [score3_1, score3_2, score3_3]]
    In this above example score1_1 is player1's score for round 1. Score3_1 is player 3's score for round 1. Score 2_3 is player 2's score for round3 
    Hence each list element in game will represent a player
    Each score (int) element in the nested list element will represent a round for that player
    Finally return a gameset list which has the game list, players list, and number of rounds
    return: list:gameset (Eg gameset returned will be a list [game, players, roundcount]. In the gameset list game is lit, players is list and roundcount is integer)
    """ 
    players = getplayers() # Calling getplayers and getting player list 
    roundCount = getrounds() # Calling getrounds and getting roundcount 
    game = [[0] * roundCount for _ in range(len(players))] # Initialize the game score board
    return [game, players, roundCount]

# 1 Marks 
def asktoroll(player): 
    """
    function: This function takes player name and asks player to hit enter to roll the dice. 
    When user hit enter calls the rolldice function and returns a score 
    :param string:player (player input is string called player name)
    :return int:score (Returns score from roll dice)
    """
    input(f"{player}! Hit enter once you are ready to roll your dices!")
    return rolldice() 

# 2 Marks 
def findwinner(game, players):
    """
    function: This function takes game list (2D list) and the player list as input parameters. Goes through the game and find the player that has the highest score
    Return the winning player name as string. If more than one player winning (eg: same score) return a winner string with all players comma seperated (Eg: John, Kate)
    :param list:game (Game list)
    :param list:players (Players list)
    :return string:winner (Winning players name as string)
    """ 
    totals = [sum(scores) for scores in game]
    maxScore = max(totals)
    winners = [players[i] for i, score in enumerate(totals) if score == maxScore]
    return ','.join(winners) 

# 5 Marks 
def rungame():
    """
    function: This function runs the game 
    It sets the game first using setgame() function. It gets the game, players and roundcount from setgame
    It prints the header and Round 1 begining score card first with inital scores set to 0
    It then asks use to roll dices using asktoroll function for all rounds and players 
    When the game finish it prompts for continuation and if chose to continue run the game again otherwise terminate.
    """

    while True:
        gameset = setgame() # Calling the setgame to get game info 
        game = gameset[0] # Getting game list 
        players = gameset[1] # Getting playerlist 
        roundCount = gameset[2] # Getting roundcount 
        printgame(game, players, 0, roundCount) # Calling printgame to print the first score card. 

        for roundNum in range(roundCount):
            for i, player in enumerate(players):
                score = asktoroll(player)
                game[i][roundNum] = score
            printgame(game, players, roundNum + 1, roundCount)

        winner = findwinner(game, players)
        print(f"Congratulation {winner}! You are our WINNER!")
        
        playAgain = input("Would you like to play another game?\n[1] Yes\n[2] No\nYour choice: ")
        if playAgain != '1':
            break

# 5 Marks
def printgame(game, players, roundNum, roundCount): 
    """
    This function takes in game list, players list, round number (aka which round is active), totalround count as input parameters
    The function prints left aligned pretty table of the game with Rounds in columns and players in rows 
    Sample Output:
    ****************** End of Round 3 ******************
            Round 1   Round 2   Round 3   Total     
    Appla     8         7         4         19        
    Applb     11        5         8         24        
    Applc     9         3         5         17        
    Appld     8         8         7         23        
    ****************************************************
    The Stars and the Round title (End of Round) are calculated and aligned as number of rounds changes. 
    This function does not return anything
    """
    header = getHeader(roundNum, roundCount)
    print(header)
    print(getTitles(players, roundCount))
    print(getScoreBoard(players, game))
    print(getFooter(len(header)))

def getHeader(roundNum, roundCount):
    return f"{'*' * int((roundCount/2)*10)}{'End of Round '+str(roundNum) if roundNum else 'Round 1'}{'*' * int((roundCount/2)*10)}"

def getFooter(len):
    return '*' * len

def getTitles(players, roundCount):
    titles = f"{'Player':<{getMaxNameLength(players)}}"
    for r in range(1, roundCount + 1):
        titles += f"Round {r:<4}"
    titles +="Total"
    return titles

def getScoreBoard(players, game):
    record = ""
    for i, player in enumerate(players):
        record += f"{player:<{getMaxNameLength(players)}}"
        total = 0
        for roundScore in game[i]:
            total += roundScore
            record += f"{roundScore:<10}"
        record += f"{total}\n"
    return record

def getMaxNameLength(players):
    maxLength = 10
    for player in players:
        if len(player) > maxLength:
            maxLength = len(player)
    return maxLength

def game():
    """
    function: Game function to run game 
    """
    rungame() # calling run game 

if __name__ == "__main__":
    """
    Main code block to run the code
    """
    game() # calling game in main block