text = input("camelCase: ")
print("snake_case: ", end='')

for c in text:
    if c.islower() == True:
        print(c, end='')
    if c.isupper() == True:
        print("_" + c.lower(), end='')
print("")
