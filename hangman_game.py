import random

# List of words
words = [
    "python",
    "computer",
    "developer",
    "programming",
    "internship",
    "software",
    "keyboard",
    "hangman"
]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 40)
print("         HANGMAN GAME")
print("=" * 40)

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong!")
        print("Remaining Attempts:", max_wrong_guesses - wrong_guesses)

if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)
