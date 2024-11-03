hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

word = input("Kelimeyi girin: ")
wordLength = len(word)
lettersInWord = list(word)
correctLetters = []
usedLetters = []
count = 0
while (True):
    for element in word:
        if element in usedLetters:
            print(element, end=" ")
        elif element == " ":
            print("/ ", end="")
        else:
            print("_ ", end="")
    newLetter = input(" ")
    if correctLetters == lettersInWord:
        print(word)
        print("Kazandınız.")
    if newLetter in usedLetters:
        print("Harf daha önce girildi")
    else:
        usedLetters.append(newLetter)
        if newLetter not in word:
            count += 1
            if (count < 6):
                print(hangman[count])
                print("Bulunmayan harfler: ", end="")
                for letter in usedLetters:
                    if letter not in word:
                        print(letter, end=" ")
                print("")
            if count == 6:
                print(hangman[6])
                print("Hak bitti")
                break
        else:
            correctLetters.append(newLetter)
            if correctLetters == lettersInWord:
                print(word)
                print("Kazandınız.")
                break


