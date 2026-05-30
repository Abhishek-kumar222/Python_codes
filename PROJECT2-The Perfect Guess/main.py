import random

cpu = random.randint(1, 100)

a = -1
guesses = 0

while a != cpu: # always true
    guesses += 1
    a = int(input("Guess the number: "))

    if a > cpu:
        print("Lower number please")

    elif a < cpu:
        print("Higher number please")

print(f"You have guessed the number correctly in {guesses} attempts")