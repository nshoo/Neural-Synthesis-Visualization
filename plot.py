from PIL import Image
import re

f = open("program.txt", 'r')
data = f.read()
f.close()

expr = re.compile("b(\d{1,}_\d{1,})")
coords = [(int(pair[0]), int(pair[1])) for pair in [pair.split('_') for pair in expr.findall(data)]]

img = Image.new("RGB", (28, 28))
pixels = img.load()

for coord in coords:
    pixels[coord[0], coord[1]] = (255, 0, 0)

scaled = img.resize((img.width * 100, img.height * 100), Image.BOX)
scaled.show()