"""
Nimm is an ancient game of strategy that is named after the old German word for "take."
 It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. 
 Players alternate taking stones until there are zero left. 
 The game of Nimm goes as follows:

1.The game starts with a pile of 20 stones between the players

2.The two players alternate turns

3.On a given turn, a player may take either 1 or 2 stone from the center pile

4.The two players continue until the center pile has run out of stones.

5.The last player to take a stone loses.
"""

def main():
    #setting stone numbers
    #telling users how mnay stones are left keepin their count
    stones = 20
    print(f"There are {stones} stones left.")

    #Create a while loop that runs until all stones are take out of game
    while stones >0:
        #Creating player variables of type int 
        #asking them how many stones they wanna remove
        player_1= int(input("Player 1 would you like to remove 1 or 2 stones? "))
        
        #creating a loop that handles wrong input apart from 1 or 2
        while player_1 not in (1,2):
            player_1=int(input("Please enter 1 or 2: "))

        #assinging if/elif statements to user input
        if player_1==1:
            print()
            stones-=1
            print(f"There are {stones} stones left.")

        elif player_1==2:
            print()
            stones-=2
            print(f"There are {stones} stones left.")

        #Break the loop when stones end at player 1 turn declear player 2 winner
        if stones <=0:
            print()
            print("Player 2 wins")
            break

        #player 2's turn

        player_2=int(input("Player 2 would you like to remove 1 or 2 stones? "))

        #same while loop for invalid input
        while player_2 not in (1,2):
            player_2=int(input("Please enter 1 or 2: "))

        #same if/elif codnitions for player 2
        if player_2==1:
            print()
            stones-=1
            print(f"There are {stones} stones left.")

        elif player_2==2:
            print()
            stones-=2
            print(f"There are {stones} stones left.")

        if stones <=0:
            print()
            print("Player 1 won!!")
            break






main()