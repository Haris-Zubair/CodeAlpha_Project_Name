import random

# List of words to choose from
words = ["python", "java", "computer", "programming", "hangman", "software", "developer"]

# Function to select a random word
def select_random_word(words):
    return random.choice(words)

# Function to display the game status
def display_status(word, guessed_letters, attempts_left):
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("\nWord:", display_word)
    print("Guessed letters:", " ".join(guessed_letters))
    print("Attempts left:", attempts_left)

# Function to play the Hangman game
def play_hangman():
    word = select_random_word(words)
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    
    while attempts_left > 0:
        display_status(word, guessed_letters, attempts_left)
        guess = input("Guess a letter: ").lower()

        # Check if input is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # If letter is already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add guess to guessed letters
        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word:
            print("Good guess!")
            # Check if all letters are guessed
            if all(letter in guessed_letters for letter in word):
                display_status(word, guessed_letters, attempts_left)
                print("Congratulations! You've won the game!")
                break
        else:
            attempts_left -= 1
            print("Incorrect guess.")

        # If attempts run out
        if attempts_left == 0:
            display_status(word, guessed_letters, attempts_left)
            print(f"Game Over! The word was '{word}'.")

# Start the game
play_hangman()
