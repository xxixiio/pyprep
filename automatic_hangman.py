to_guess = input("Word to guess:").upper()
list_to_guess = to_guess.split()

print("_" * len(to_guess))

guessed = False
used_letters = []
lives = 7

while (lives > 0) and (not guessed):
    guessing_letter = input("Enter a letter: ").upper()[0]
    if guessing_letter in list_to_guess:
        if guessing_letter in used_letters:
            print("Repeated letter. {lives} lives.")
        
    
if lives > 0:
    print("You losed. The word to guess was {to_guess}")
elif guessed:
    print("You won. The word to guess was {to_guess}")