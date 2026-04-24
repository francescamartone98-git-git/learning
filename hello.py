import random


name = input ("What's your name?") 
surname = input ("what's your surmane?")

secret = random.randint(1, 10)
guess = 0
attempts = 0

while attempts <= 3:
    guess = int(input("Guess the number between 1 and 10: "))
    attempts += 1
    
    if guess == secret:
        print(f"you've got it in {attempts}!")
        break
    elif guess < secret:
        print("too low!")
    else:
        print("too high")


if guess != secret:
    print(f"sorry, the numeber was {secret}")