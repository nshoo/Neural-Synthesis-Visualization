from venv import create
from tensorflow import keras
from classify import classify_image
from tqdm import tqdm
import os

digit_names = ["zeros", "ones", "twos", "threes", "fours", "fives", "sixes", "sevens", "eights", "nines"]

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

def create_digit(img, rpad):
    built = ""
    for row in img:
        for pix in row:
            built += '█' if pix > 0 else ' '
        built += ' ' * rpad
        built += '\n'
    return built

def display_digit(img):
    print(img, 0)

def print_centered(text):
    term_size = os.get_terminal_size()
    print(text.center(term_size.columns, ' '))

def print_bar(length):
    print("=" * length)

def print_full_bar():
    term_size = os.get_terminal_size()
    print_bar(term_size.columns)

def print_with_bar(text):
    print(text)
    print_bar(len(text))

# will be true
left_digit = 1
# will be false
right_digit = 7

left_test = [x_test[i] for i in range(len(x_test)) if y_test[i] == left_digit]
right_test = [x_test[i] for i in range(len(x_test)) if y_test[i] == right_digit]

term_size = os.get_terminal_size()

print_centered(f"Running tests for {digit_names[left_digit]} and {digit_names[right_digit]}:")
print_full_bar()
for line in [''.join(x) for x in zip(create_digit(left_test[0], 5).split('\n'), create_digit(right_test[0], 0).split('\n'))]:
    print_centered(line)

n = 100
left_accuracy = sum([1 if not classify_image(list(left_test[i])) else 0 for i in tqdm(range(n))]) / n
right_accuracy = sum([1 if classify_image(list(right_test[i])) else 0 for i in tqdm(range(n))]) / n

print('')
print_with_bar("Results:")
print(f"Accuracy for {digit_names[left_digit]}: {left_accuracy}")
print(f"Accuracy for {digit_names[right_digit]}: {right_accuracy}")