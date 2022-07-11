from tensorflow import keras
from classify import classify_image

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

def display_digit(img):
  for row in img:
    for pix in row:
      print('█' if pix > 0 else ' ', end='')
    print('')

ones = [x_test[i] for i in range(len(x_test)) if y_test[i] == 1]
sevens = [x_test[i] for i in range(len(x_test)) if y_test[i] == 7]

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