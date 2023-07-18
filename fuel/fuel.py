while True:
    try:
        fuel = input("Fraction: ")
        int1, int2 = fuel.split("/")
        int1, int2 = int(int1), int(int2)
        percentage = round(int1/int2 * 100)

    except (ValueError, ZeroDivisionError):
        pass

    else:
        if int1 > int2:
            pass
        elif percentage <= 1:
            print ("E")
            break
        elif percentage >= 99:
            print("F")
            break
        else:
            print(f"{percentage}%")
            break
