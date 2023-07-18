shopping_list = {}

while True:
    try:
        item = input("")

    except EOFError:
        print()
        break

    if item not in shopping_list:
        shopping_list[item] = 1
    else:
        shopping_list[item] += 1


for item in sorted(shopping_list):

    print(shopping_list[item], (f"{item}").upper())
