from datetime import date
import inflect
import sys


def main():
    print(convert(input("Date of Birth: ")))


def convert(date_str):
    try:
        # Split date into year, month and day
        year, month, day = date_str.split("-")
        # Pass "date" object to "birth_date"
        birth_date = date(int(year), int(month), int(day))

    except ValueError:
        sys.exit("Invalid date")

    # Get today's date
    today = date.today()
    # Get total amount of minutes between birth date and today's date
    result1 = today - birth_date
    result2, _ = str(result1 * 1440).split(' ', 1)
    # Convert minutes from int to words string
    result2 = inflect.engine().number_to_words(result2)
    # Return capitalized str of minutes with all the ' and' erased
    return f"{result2.capitalize().replace(' and', '')} minutes"


if __name__ == "__main__":
    main()