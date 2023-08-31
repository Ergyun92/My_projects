import random
import time

print("Hangman's game")
print("--------------")

list_of_words = ["backend", "computer", "vacation", "fantastic", "delicious", "suave"]
picked_letters = []
secret_word = random.choice(list_of_words)
lives = 5
time.sleep(2)
while True:
    choice = input("Choose a letter: ").lower()

    if choice in picked_letters:
        print("You have tried that before")
        continue
    picked_letters.append(choice)

    if choice in secret_word:
        print("You have found a letter")
    else:
        print("Nope, that's not in there")
        lives -= 1

    all_letters = True

    for i in secret_word:
        if i in picked_letters:
            print(i, end="")
        else:
            print("_", end="")
            all_letters = False
    print()

    if all_letters:
        print(f"You won with {lives} lives left!")
        break
    if lives <= 0:
        print("You ran out of lives! Game over")
        break
    else:
        print(f"You have {lives} lives left")