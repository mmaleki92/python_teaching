import random

# List of possible words to guess
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry']

# Select a word at random
word = random.choice(words)

# Set up the game
guesses = ''
turns = 6

# Loop until the player runs out of turns or guesses the word
while turns > 0:
    # Show the player the current state of the word
    progress = ''
    for letter in word:
        if letter in guesses:
            progress += letter
        else:
            progress += '_'
    print(progress)
    
    # Ask the player for their guess
    guess = input("Guess a letter: ")
    guesses += guess
    
    # Check if the guess is in the word
    if guess not in word:
        turns -= 1
        print("Incorrect! You have", turns, "turns left.")
        
    # Check if the player has guessed the whole word
    if '_' not in progress:
        print("Congratulations! You guessed the word:", word)
        break

# If the player runs out of turns, reveal the word
if turns == 0:
    print("Sorry, you ran out of turns. The word was", word)
