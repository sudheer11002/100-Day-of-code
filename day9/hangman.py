
word_list = ["Shivi", "shivani", "paro"]

import random
chosen_word = random.choice(word_list)

guess = input("Guess the girl: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
