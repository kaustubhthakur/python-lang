import random

def get_choices():
    player_choice = input("enter a choice\n")
    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options);
    choices = {"player":player_choice,"computer":computer_choice}

    return choices

def check_win(player,computer):
    print("you chose"+player+"computer chose"+computer)
    if player==computer:
        return "its a draw"
    elif player=="rock" and computer=="scissors":
        return "your lose"
    elif player=="rock" and computer=="paper":
        return "your loss"
        

