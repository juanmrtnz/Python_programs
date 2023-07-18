def main():
    text = input()
    print(convert(text))


def convert(t):
    return t.replace(':)', '🙂').replace(':(', '🙁')


main()