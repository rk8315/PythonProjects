import random
import art
import words

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(words.word_list)
display = []
letters_guessed = []
number_of_lives = 6
game_over = False

print(art.logo)

for space in chosen_word:
    display.append("_")

print("Your word is:")
print(display)

# TESTING CODE
# print(chosen_word)

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in letters_guessed:
        print(f"Your have already selected {guess}")
    else:
        letters_guessed.append(guess)
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = guess

        if guess not in chosen_word:
            number_of_lives -= 1
            print(f"The letter {guess} is not in the word.")
            if number_of_lives == 0:
                game_over = True
                print("***You Lose!***")

        print(f"Number of lives: {number_of_lives}")
        print(f"{' '.join(display)}")

        if "_" not in display:
            game_over = True
            print("***You win!***")

        print(art.stages[number_of_lives])