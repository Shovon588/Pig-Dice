from utils import *


while(1):
    print("1. Play with player")
    print("2. Play with computer")
    print("3. Quit")
    play_with = int(input("Your answer (1/2/3)): "))
    if play_with==3:
        print("See you soon!")
        break
    
    winning_score = int(input("Please set a winning score. To leave it default (100) enter 0: "))

    player1 = 0
    player2 = 0
    lastone = 0
    number = 0
    who = 1
    
    if play_with==1 or play_with==2:
        play(player1,player2,lastone,number,who,play_with, winning_score)        
    else:
        print("Invalid response. Please choose again.")
