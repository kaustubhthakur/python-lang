#dictionary - used to store key value pair {"key":"value"} 
#list - used to store multiple items []
import random
def get_choices():
    player_choice = input("enter a choice !! rock ,paper or scissors \n");
    options = ["rock","paper","scissors"]
    computer_choice = random.choice(options);
    choices = {"player":player_choice,"computer":computer_choice}

    return player_choice


def check_win(player,computer):
    print(f"you choose {player}, computer chose {computer}")

    if player==computer:
        return "its a draw"
    elif player=="rock" and computer=="scissors":
        return "your win"
    elif player=="rock" and computer=="paper":
        return "your loss"

choices = get_choices()
result =check_win(choices["player"],choices["computer"])
print("result",result);