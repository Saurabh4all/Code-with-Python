actual_number = 45
attempts = 0
#Number Guessing Game Pro 1
while True:
    attempts +=1
    guess = int(input ("Guess the number :\n"))
    if guess < actual_number:
        print ("Your guess is too low\n")

    elif guess > actual_number:
        print ("Your guess is too high\n")

    else:
        print(f"You guessed the number in {attempts} attempts\n")
        break

print("Game over! Thanks for playing!\n")