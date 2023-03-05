import random

print("Welcome to Bible Hangman")
print("********************************************")

wordDictionary = ["Angel", "Isaiah", "Noah", "Ark", "Commandments", "Deuteronomy", "light", "Temple", "Clay", "Garden"]

### Choose a random word
randomword = random.choice(wordDictionary)

for x in randomword:
    print("_", end="")

def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+---+")
        print("o   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("o   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" o  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" o  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")

def printWord(guessedLetters):
    counter=0
    rightLetters=0
    for char in randomword:
        if(char in guessedLetters):
            print(randomword[counter], end=" ")
            rightLetters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightLetters

def printLine():
    print("\r")
    for char in randomword:
        print("\u203E", end=" ")

length_of_word_to_guess = len(randomword)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\n Letters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
        ### Prompt user for input
    letterGuessed = input("\nGuess a letter: ")
    ##### User is right
    if(randomword[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)
        ### Print word
        current_guess_index+=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLine()
        ### User was wrong
    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letterGuessed)
        ### Update the drawiing
        print_hangman(amount_of_times_wrong)
        ###Print out word
        current_letters_right = printWord(current_letters_guessed)
        printLine()

print("Game is over. Thank you for playing!")










