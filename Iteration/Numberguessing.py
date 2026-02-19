# Number guessing game

secret_number = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct guess!")
        break
    else:
        print("Try again")
