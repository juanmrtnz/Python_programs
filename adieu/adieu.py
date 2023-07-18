nameslist = []

while True:
    try:
        name = input("Name: ")
        nameslist.append(name)
    except EOFError:
        print()
        break

if len(nameslist) == 0:
    print("Not enough names")
elif len(nameslist) == 1:
    print("Adieu, adieu, to " + name)
elif len(nameslist) == 2:
    print("Adieu, adieu, to " + nameslist[0] + " and " + nameslist[1])
elif len(nameslist) > 2:
    print("Adieu, adieu, to ", end='')
    for name in nameslist:
        if name == nameslist[len(nameslist) - 1]:
            print("and " + name)
        else:
            print(name + ", ", end='')
