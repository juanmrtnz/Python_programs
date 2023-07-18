import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # If input is formatted correctly
    if matches := re.search(r'^(\d+):?(\d{2})? (AM|PM) to (\d+):?(\d{2})? (AM|PM)$', s):
        # Pass groups to variables and raise errors if hours > 12 or minutes > 59
        hour1 = int(matches.group(1))
        hour_format1 = matches.group(3)
        hour2 = int(matches.group(4))
        hour_format2 = matches.group(6)

        if hour1 > 12 or hour2 > 12:
            raise ValueError
        if matches.group(2):
            if int(matches.group(2)) > 59:
                raise ValueError
        if matches.group(5):
            minute2 = int(matches.group(5))
            if minute2 > 59:
                raise ValueError

        # Change AM/PM formatted hours to 24h formatted ones
        if hour_format1 == 'AM' and hour1 == 12:
            hour1 = 0
        if hour_format2 == 'AM' and hour2 == 12:
            hour2 = 0
        if hour_format1 == 'PM':
            if hour1 == 12:
                hour1 = 12
            else:
                hour1 += 12
        if matches.group(2):
            minute1 = int(matches.group(2))
        else:
            minute1 = 0
        if hour_format2 == 'PM':
            if hour2 == 12:
                hour2 = 12
            else:
                hour2 += 12
        if matches.group(5):
            minute2 = matches.group(5)
        else:
            minute2 = 0

        return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
    # If format is incorrect, raise error
    else:
        raise ValueError


if __name__ == "__main__":
    main()