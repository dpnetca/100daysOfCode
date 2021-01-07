import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = len(stages) - 1

print(logo)

display = ["_"] * word_length
guessed_letters = []

while not end_of_game:
    print(stages[lives])
    print(f"{' '.join(display)}\n")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You have already guessed {guess}")
    else:
        guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    else:
        print(f"{guess} is incorrect")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"the word was {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
