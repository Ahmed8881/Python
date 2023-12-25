import random as rn
from termcolor import colored

random_number = rn.randint(1,100)

choice = input("Choose an option: 'easy' or 'hard' ").lower()
while not choice in ["easy", "hard"]: 
    print("Invalid Input.")
    choice = input("Choose an option: 'easy' or 'hard' ").lower()

attempts = 10 if choice == "easy" else 5

while(attempts != 0):

    guess = input("Enter your guess: ")
    while not guess.isdigit():
        print("Invalid Input")
        guess = input("Enter your guess: ")
    guess = int(guess)
    
    if guess < random_number:
        print(colored("Too low","red"))
        attempts -= 1
    elif guess > random_number:
        print(colored("Too high","magenta"))
        attempts -= 1
    else:
        print("Congratulations you guessed the number.")
        print(colored(f"The number was {random_number}","green"))
        break
    print(f"You have {attempts} attempts remaining")