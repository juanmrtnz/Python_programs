import random

while True:
    try:
        level = int(input("Level: "))
        random_number = random.randint(1, level)
        break

    except ValueError:
        pass


while True:
    try:
        guess = int(input("Guess: "))

        if guess < random_number:
            print("Too small!")
            pass

        elif guess > random_number:
            print("Too large!")
            pass

        elif guess == random_number:
            print("Just right!")
            break

    except ValueError:
        pass
