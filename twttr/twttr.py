text = input("Input: ")
for c in text:
    if c.lower() == 'a' or c.lower() =='e' or c.lower() =='i' or c.lower() =='o' or c.lower() =='u':
        print("", end='')
    else:
        print(c, end='')
print("")