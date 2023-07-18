def main():
    text = input("Fraction: ")
    text = convert(text)
    print(text)
    print(gauge(text))



def convert(fraction):
        try:
            int1, int2 = fraction.split("/")
            int1, int2 = int(int1), int(int2)
            if int2 == 0:
                raise ZeroDivisionError
            if int1 > int2:
                raise ValueError
            return round(int1/int2 * 100)

        except ValueError:
            raise ValueError


def gauge(percentage):
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return f"{percentage}%"


if __name__ == "__main__":
    main()