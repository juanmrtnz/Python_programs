def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() == True and 4 <= (s.count('') - 1) <= 6:
        for char in s:
            if char.isdigit():
                if char == '0':
                    return False
                else:
                    break
        for char in s:
            if char.isdigit() and s[s.index(char):len(s)].isdigit() == False:
                return False
            if char == ' ' or char == '.' or char == ',':
                return False
        return True


main()