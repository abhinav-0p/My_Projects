import random as rd
from emoji import emojize as emo

class Game:
    def __init__(self,name):
        self.name = name
        self.health = 120

    def roll(self):
        num = rd.randint(1,6)
        return num


players = []
print("-"*5,"Welcome to Dice Battle","-"*5)
for i in range(1,3):
    name = input(f"Enter player {i} name : ")
    g = Game(name)
    players.append(g)


while players[0].health>0 and players[1].health>0:
    print()
    print("-"*18)
    print(emo(":crossed_swords:  Dice Battle :crossed_swords:"))
    print("-"*18,"\n")
    player_1 = input(f"{players[0].name}'s turn!! Type(R) :")
    if player_1:
        num1 = players[0].roll()
        print(f"You got {num1}")
    
    player_2 = input(f"{players[1].name}'s turn!! Type(R) :")
    if player_2:
        num2 = players[1].roll()
        print(f"You got {num2}\n")
    
    if num1 > num2:
        print(emo(f"{players[0].name} won this round :fire:\n"))
        players[1].health-=(num1-num2)*10
        if players[1].health <= 0:
            print(f"{players[1].name} lost the Battle")
        else:
            print(f"{players[1].name}'s health has been cut down by {(num1-num2)*10}\n")
            print(f"{players[1].name} Health : {players[1].health}/120")
            print(f"{players[0].name} Health : {players[0].health}/120\n")
    elif num2>num1:
        print(emo(f"{players[1].name} won this round :fire:\n"))
        players[0].health-=(num2-num1)*10
        if players[0].health <= 0:
            print(f"{players[0].name} lost the Battle")
        else:
            print(f"{players[0].name}'s health has been cut down by {(num2-num1)*10}\n")
            print(f"{players[0].name} Health : {players[0].health}/120")
            print(f"{players[1].name} Health : {players[1].health}/120\n")
    else:
        print("its a draw....")

if players[0].health <= 0:
    print(emo(f":confetti_ball: Congratulation {players[1].name}, You Won The Battle :confetti_ball:"))
elif players[1].health <= 0:
    print(emo(f":confetti_ball: Congratulation {players[0].name}, You Won The Battle :confetti_ball:"))







# :crossed_swords:
# :confetti_ball: