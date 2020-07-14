import random
import time
import sys


def roll_dice():
    return random.randint(1,6)


def print_result(player1, player2):
    print("#############################")
    print("##     Current Score:      ##")
    print("##                         ##")        
    print("   Player: %d | Computer: %d" %(player1,player2))
    print("#############################")


def computers_turn(who,computer,number,lastone):
    time.sleep(2)
    number = roll_dice()
    if number==1:
        computer = 0
        who+=1
    else:
        computer+=number
        
        if lastone>6:
            who+=1
    return who,computer,number,lastone


def players_turn(who,player,number,lastone):
    print("1. Roll Dice\t2. Transfer Dice\t3. Quit Match")
    decision = input("What do you want? (1/2/3): ")
    
    if decision=='3':
        print("Too bad to see you go.\nHope to see you soon.")
        sys.exit(0)
    elif decision=='2':
        who+=1
    elif decision=='1':
        number = roll_dice()
        if number==1:
            print("Uh oh.")
            player=0
            who+=1
        else:
            player+=number
    else:
        print("Invalid response. Choose again.")

    return who,player,number,lastone
    

def declare_winner(p1name, p2name, p1score, p2score, winning_score=100):
    if p1score>=winning_score:
        print("\n%s wins. Congratulations." %(p1name))
        print_result(p1score,p2score)
        sys.exit(0)
    elif p2score>=winning_score:
        print("\n%s wins. Congratulations." %(p2name))
        print_result(p1score,p2score)
        sys.exit(0)



def play(player1,player2,lastone,number,who,play_with,winning_score):
    while True:
        print("---------------------------------------------------\n")
        if number>0:
            print("Previous number: %d"%(number))
        if who%2==1:
            if play_with==1:
                print("Player1's turn")
            else:
                print("Player's turn")
            who,player1,number,lastone = players_turn(who,player1,number,lastone)
        else:
            if play_with==1:
                print("Player2's turn")
                who,player2,number,lastone = players_turn(who,player2,number,lastone)
            else:
                print("Computer's turn")
                who,player2,number,lastone = computers_turn(who,player2,number,lastone)
            

        if number!=1:
            lastone+=1
        else:
            lastone=0

        if play_with==1:
            declare_winner("Player1","Player2",player1,player2,winning_score)
        else:
            declare_winner("Player","Computer",player1,player2,winning_score)
        

        print_result(player1,player2)


    
