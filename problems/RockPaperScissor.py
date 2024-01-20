import random

def play():
    user = input("'r' for rock, 'p' for paper , 's' for sciccors")
    computer = random.choice(['r','p','s'])

    if user == computer:
        print("tie!")

    if win(user,computer):
        print('you won!')

    if win(computer,user):
        print('you lost!')

def win(player , opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

play()        