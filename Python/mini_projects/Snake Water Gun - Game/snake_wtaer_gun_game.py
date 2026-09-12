import random2
choices = ["snake", "water" , "gun"]

user1 = input("choose any one---> SNAKE / WATER / GUN :")
user2 = random2.choice(choices)

lower_user1 = user1.lower()
lower_user2 = user2.lower()

print("Player selected",lower_user1)
print("Computer jii selected",lower_user2)

if((lower_user1 == "snake") and (lower_user2 == "water")):
    print("Snake won")
elif((lower_user1 == "snake") and (lower_user2 == "gun")):
    print("gun won")
elif((lower_user1 == "water") and (lower_user2 == "snake")):
    print("snake won")
elif((lower_user1 == "water") and (lower_user2 == "gun")):
    print("water won")
elif((lower_user1 == "gun") and (lower_user2 == "snake")):
    print("gun won")
elif((lower_user1 == "gun") and (lower_user2 == "water")):
    print("water won")
elif(lower_user1 == lower_user2 ):
    print("it's a draw")
else:
    print("Please provide valid input")