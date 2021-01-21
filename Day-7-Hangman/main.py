import random
from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear

print(logo)

word_list = word_list
chosen_word = random.choice(word_list)
display = []
lives = 6

for i in range(len(chosen_word)):
    display.append("_")
print(display)  # 幾個字母

while True:
    guess = input("Guess a letter:\n").lower()
    clear()

    if guess in display:
        print(f"You have already gurssed {guess}")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]

    if guess not in chosen_word:
        print(f"{guess} is not in the word")
        lives -= 1
        if lives == 0:  # lose condition
            print("You lose")
            break

    print(f"{' '.join(display)}")

    # win condition
    if "_" not in display:
        print("You win!!")
        break

    # how many lives left
    print(stages[lives])
