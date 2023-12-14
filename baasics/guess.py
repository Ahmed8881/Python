from random import randint as rn

NUMBER = rn(1, 100)

print("The number in my mind is between 1 and 100.")
choice = input("Do you want to play in 'easy' or 'hard' mode? ")
while not choice.lower() in ["easy", "hard"]:
    print("Invalid choice. Try again.")
    choice = input("Do you want to play in 'easy' or 'hard' mode? ")

if choice == "easy":
    attempts = 10
else:
    attempts = 5


while attempts != 0:
    print(f"You have {attempts} attempts remaining.")

    guess = input("Enter your guess: ")
    while not guess.isdigit():
        print("Invalid input. Try again.")
        guess = input("Enter your guess: ")
    guess = int(guess)

    if guess > NUMBER:
        print("Too high.")
        attempts -= 1
    elif guess < NUMBER:
        print("Too low.")
        attempts -= 1
    else:
        print("Congratulations, you managed to guess the number.")
        break

if attempts == 0:
    print("You ran out of attempts.")
print(f"The number was {NUMBER}")