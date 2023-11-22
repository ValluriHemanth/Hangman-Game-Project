import random
#Greet

print("Welcome to Hangman Game ")
name = input("Enter your name: ")


print(f"Hello🙋! {name}")

words =['apple','Bat','Cat','fog']

word_to_guess = random.choice(words)
attempts=0
max_attempts = 7
guessed_letter=[]

while True:

    display = ""

    for letter in word_to_guess:

        if letter in guessed_letter:
            display+=letter
        else:
            display+="_"

    print(display)

    if display==word_to_guess:

        print("Congratulations🏆 you have guessed word correctly")
        break 

    if attempts>=max_attempts:
        print("Sorry you ran out of attempts")
        break

    guess = input("Enter the letter: ").lower()

    if len(guess)>1 or not guess.isalpha():

        print("Please enter a single letter ")

        continue

    if guess in guessed_letter:
        print("You have already guessed this letter")
        continue

    guessed_letter.append(guess)

    if guess not in word_to_guess:

        attempts+=1

        print("Incorrect guess. Attempts remaining: ",max_attempts-attempts)


        if attempts == 1:
            print("  +---+")
            print("  |   |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("     -----")
        elif attempts == 2: 
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print("      |")
            print("      |")
            print("      |")
            print("     -----")
        elif attempts == 3:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print("  |   |")
            print("      |")
            print("      |")
            print("     -----")
        elif attempts == 4:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|   |")
            print("      |")
            print("      |")
            print("     -----")
        elif attempts == 5:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\\  |")
            print("      |")
            print("      |")
            print("     -----")

        elif attempts == 6:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\\  |")
            print(" /    |")
            print("      |")
            print("     -----")
        elif attempts == 7:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\\  |")
            print(" / \\  |")
            print("      |")
            print("     -----")



    










