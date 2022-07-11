from tensorflow import keras
from classify import classify_image
from numpy import array

def display_digit(img):
  for row in img:
    for pix in row:
      print('█' if pix > 0 else ' ', end='')
    print('')

file = open("array.txt", "r")
data = file.read()
file.close()

digits = eval(data)


display_digit(ones[1])

n = 100
countSevens = 0
countOnes = 0
for i in range(n):
    imageSevens = classify_image(list(sevens[i]))
    imageOnes = classify_image(list(ones[i]))
    print(imageOnes, imageSevens)
    if imageSevens:
        countSevens += 1
    if not imageOnes:
        countOnes += 1

accuracySevens = countSevens/n    
accuracyOnes = countOnes/n
print(f"Sevens: {accuracySevens} Ones: {accuracyOnes}")