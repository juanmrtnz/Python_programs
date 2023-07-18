def main():
    answer = input('Greeting: ')
    print("$"+ str(value(answer)))



def value(greeting):
    if greeting.strip().lower().startswith('hello') == True:
        return 0
    elif greeting.strip().lower().startswith('h') == True:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()