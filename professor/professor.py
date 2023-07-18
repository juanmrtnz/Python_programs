import random


def main():
    # Get level from user
    level = get_level()
    # Generate 2 integers for the sum
    int1, int2 = generate_integer(level), generate_integer(level)
    #Set correct answers to 0
    correct_answers = 0
    # Set errors to 0
    errors_number = 0
    # Set loops to 0
    loops = 0
    while True:
        if loops == 10:
            break
        try:
            # Give user sum of the 2 int and prompt for answer
            second_answer = int(input(str(int1) + " + " + str(int2) + " = "))
            # If answer is correct, add 1 correct answer, generate 2 other int and add 1 to loops
            if (int1 + int2) == second_answer:
                correct_answers += 1
                int1, int2 = generate_integer(level), generate_integer(level)
                loops += 1
            # If answer is incorrect, add 1 error
            else:
                errors_number += 1
            # If errors is 1 or 2, print "EEE"
            if 0 < errors_number < 3:
                print("EEE")
            # If errors is 3, set it to 0, print the answer, generate 2 other int and add 1 to loops
            if errors_number == 3:
                errors_number = 0
                print(str(int1) + " + " + str(int2) + " = " + str(int1+int2))
                int1, int2 = generate_integer(level), generate_integer(level)
                loops += 1
        # If answer is not an int
        except ValueError:
            # Add 1 error
            errors_number += 1
            # If errors is 1 or 2, print "EEE" and pass to try
            if 0 < errors_number < 3:
                print("EEE")
                pass
            # If errors is 3, set it to 0, print the correct answer, generate 2 other int, add 1 to loops and pass to try
            if errors_number == 3:
                errors_number = 0
                print(str(int1) + " + " + str(int2) + " = " + str(int1+int2))
                int1, int2 = generate_integer(level), generate_integer(level)
                loops += 1
                pass

    # After while loop, print score
    print("Score:", correct_answers)


def get_level():
    while True:
        try:
            # Prompt user for answer as int
            first_answer = int(input("Level: "))
            # Return only if answer is 1, 2 or 3, else keep prompting
            if first_answer == 1 or first_answer == 2 or first_answer == 3:
                return first_answer
            else:
                pass
        # If answer is not an int, keep prompting
        except ValueError:
            pass


def generate_integer(x):
    # Randomly generate an integer of x digits
    if x == 1:
        return random.randint(0, 9)
    elif x == 2:
        return random.randint(10,99)
    elif x == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()