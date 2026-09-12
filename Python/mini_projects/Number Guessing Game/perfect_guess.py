import random2
random_no = random2.randint(1,50)

a = -1
# print(f"guessed:{random_no}")
attempt = 0
while(a != random_no):
    attempt = attempt + 1
    p_guess = int(input("Guess the number between 1-50:"))

    if(p_guess == random_no):
        print("Congrats , you guessed the number")
        break
    elif(p_guess < random_no):
        print("Your number is smaller")
    elif(p_guess > random_no):
        print("Your number is greater")
    else:
        print("error")

print(f"you guessed the number {p_guess} in {attempt} attempt")