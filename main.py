import random
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def display_title():
    print("Welcome to Bible Hangman")
    print("********************************************")

wordDictionary = [
    "Angel", "Isaiah", "Noah", "Ark", "Commandments", 
    "Deuteronomy", "Light", "Temple", "Clay", "Garden",
    "Jesus", "Moses", "David", "Solomon", "Abraham"
]

def get_valid_input():
    while True:
        guess = input("\nGuess a letter: ").upper()
        if len(guess) != 1:
            print("Please enter a single letter!")
            continue
        if not guess.isalpha():
            print("Please enter a letter!")
            continue
        return guess

def print_hangman(wrong):
    stages = [
        "\n+---+\n    |\n    |\n    |\n   ===",
        "\n+---+\no   |\n    |\n    |\n   ===",
        "\n+---+\no   |\n|   |\n    |\n   ===",
        "\n+---+\n o  |\n/|  |\n    |\n   ===",
        "\n+---+\n o  |\n/|\ |\n    |\n   ===",
        "\n+---+\n o  |\n/|\ |\n/   |\n   ===",
        "\n+---+\n o  |\n/|\ |\n/ \ |\n   ==="
    ]
    print(stages[wrong])

def print_word(word, guessed_letters):
    displayed_word = ''
    right_letters = 0
    for char in word:
        if char.upper() in guessed_letters:
            displayed_word += char + " "
            right_letters += 1
        else:
            displayed_word += "_ "
    print(displayed_word)
    return right_letters

def play_game():
    clear_screen()
    display_title()
    
    random_word = random.choice(wordDictionary).upper()
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6
    
    print("\nYour word has", len(random_word), "letters:")
    print_word(random_word, guessed_letters)

    while wrong_guesses < max_attempts:
        print("\nLetters guessed:", " ".join(sorted(guessed_letters)))
        print(f"Attempts remaining: {max_attempts - wrong_guesses}")
        
        guess = get_valid_input()
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
            
        guessed_letters.add(guess)
        
        if guess not in random_word:
            wrong_guesses += 1
            print("\nWrong guess!")
        else:
            print("\nCorrect guess!")
            
        print_hangman(wrong_guesses)
        correct_letters = print_word(random_word, guessed_letters)
        
        if correct_letters == len(random_word):
            print("\nCongratulations! You won! 🎉")
            print(f"The word was: {random_word}")
            return True
            
    print("\nGame Over! 😢")
    print(f"The word was: {random_word}")
    return False

def main():
    while True:
        play_game()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("\nThanks for playing Bible Hangman!")
            break

if __name__ == "__main__":
    main()










