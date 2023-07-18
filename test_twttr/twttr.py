def main():
    text = input("Input: ")
    print("Output: " + shorten(text))


def shorten(word):
    new_word = ''
    for char in word:
        if char.lower() == 'a' or char.lower() == 'e' or char.lower() =='i' or char.lower() == 'o' or char.lower() == 'u':
            new_word = new_word + ''
        else:
            new_word = new_word + char
    return new_word


if __name__ == "__main__":
    main()