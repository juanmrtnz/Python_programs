import sys
from PIL import Image
from PIL import ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if sys.argv[1].lower().endswith(".jpeg") == False and sys.argv[1].lower().endswith(".jpg") == False and sys.argv[1].lower().endswith(".png") == False:
    sys.exit("Invalid input")

if sys.argv[2].lower().endswith(".jpeg") == False and sys.argv[2].lower().endswith(".jpg") == False and sys.argv[2].lower().endswith(".png") == False:
    sys.exit("Invalid output")

name1, ending1 = sys.argv[1].rsplit(".", 1)
name2, ending2 = sys.argv[2].rsplit(".", 1)

if ending1 != ending2:
    sys.exit("Input and output have different extensions")

try:
    # Open input image to "input_image"
    input_image = Image.open(sys.argv[1])
    # Open shirt.png image to "shirt"
    shirt = Image.open("shirt.png")
    # Get width and height(size) of shirt.png to "shirt_size"
    shirt_size = shirt.size
    # Resize and crop input to match shirt.png's size
    input_image = ImageOps.fit(input_image, shirt_size)
    # Paste shirt.png into input image
    input_image.paste(shirt, mask=shirt)
    # Save image to file specified in sys.argv[2]
    input_image.save(sys.argv[2])



except FileNotFoundError:
    sys.exit("Could not find " + sys.argv[1])