from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fontlist = figlet.getFonts()


if len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font=(random.choice(fontlist)))
    print(figlet.renderText(text))

elif len(sys.argv) == 3:
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fontlist:
        text = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(text))

    else:
        sys.exit("Invalid usage")

elif sys.argv[2] not in fontlist:
    sys.exit("Font name not valid")
else:
    sys.exit("Invalid usage")
