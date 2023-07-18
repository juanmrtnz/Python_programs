months_dict = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12
}


while True:
    try:
        date = input("Date: ").lower().strip()
        if date[0].isdigit() == True:
            month, day, year = date.split('/')
        elif date[0].isalpha() == True:
            month_and_day, year = date.split(', ')
            month, day = month_and_day.split(' ')
            if month in months_dict:
                month = months_dict[month]
        month, day, year = int(month), int(day), int(year)

    except ValueError:
        pass

    else:
        if month < 1 or day < 1 or year < 1:
            pass
        elif month > 12 or day > 31:
            pass
        else:
            print(str(year) + "-" + f"{month:02}" + "-" + f"{day:02}")
            break
