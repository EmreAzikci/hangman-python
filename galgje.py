from os import system
# Made by Emre Azikci - This is a school assignment!

print("## Pick a word to start playing hangman! ##")
print("## The first player gets to pick a word ##")
print("## The second player can then start guessing the word by typing in a letter ##")
print("## If the letter is guessed correctly you'll see the letter being displayed in right spot in the word ##")
print("## Good luck!! ##")

theMysteryWord = ""
correctLetters = []
wrongLetters = []
guessCount = 0
isGameDone = False


def getMysteryWord():
    # This gets the Mystery word that has been input for hangman aka galgje!
    theMysteryWord = input(
        "Pick a word to start playing hangman! Enter your word: ").lower()
    system("cls")
    return theMysteryWord


def displayBoard(theMysteryWord, correctLetters, wrongLetters):
    # This should display the status board
    print("Correct letters: " + ", ".join(correctLetters))
    print("Wrong letters: " + ", ".join(wrongLetters))

    blanks = ["-" for letter in theMysteryWord]

    # Replace the dashes with the correct letters
    for i in range(len(theMysteryWord)):
        if theMysteryWord[i] in correctLetters:
            blanks[i] = theMysteryWord[i]

    # Join the blanks list with commas for display
    mysteryWordSplitIntoDashes = ", ".join(blanks)

    print(f"The mystery word consists of {len(theMysteryWord)} letters")
    print(f"The word: {mysteryWordSplitIntoDashes}")
    return ""


def getPlayerGuess(theMysteryWord, correctLetters, wrongLetters, guessCount):
    print("## Second user can now guess a letter ##")

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) > 1:
            print("Only single letters allowed! Please type in one letter at a time.")
        elif guess in correctLetters or guess in wrongLetters:
            print(f"You've already guessed the letter '{guess}', guess again!")
        elif guess in theMysteryWord:
            correctLetters.append(guess)
            print(f"The letter '{guess}' is in the word!")
            break
        else:
            wrongLetters.append(guess)
            guessCount += 1
            print(f"The letter '{
                  guess}' is not in the word! Current wrong attempts: {guessCount}")
            break

    # Check if the word has been fully guessed
    isGameDone = all(letter in correctLetters for letter in theMysteryWord)

    # Check if the user has reached the maximum number of wrong attempts
    if guessCount >= 9:
        print("You've reached the maximum number of wrong attempts! Game over!")
        isGameDone = True

    return correctLetters, wrongLetters, guessCount, isGameDone


while True:
    theMysteryWord = getMysteryWord()
    while not isGameDone:
        displayBoard(theMysteryWord, correctLetters, wrongLetters)
        correctLetters, wrongLetters, guessCount, isGameDone = getPlayerGuess(
            theMysteryWord, correctLetters, wrongLetters, guessCount
        )

    # Display appropriate message when the game ends
    if all(letter in correctLetters for letter in theMysteryWord):
        print(f"Congratulations! You've guessed the word '{theMysteryWord}'!")
    else:
        print(f"Game over! The mystery word was '{theMysteryWord}'.")
    break
