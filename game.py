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

kelime = input("Kelimeyi girin: ")
uzunluk = len(kelime)
kullanilan_harfler = []
sayac = 0
while (True):
    for element in kelime:
        if element in kullanilan_harfler:
            print(element, end="")
        elif element == " ":
            print("/", end="")
        else:
            print("_", end="")
    newLetter = input(" ")
    kullanilan_harfler.append(newLetter)
    if newLetter not in kelime:
        sayac += 1
        if (sayac < 7):
            print(hangman[sayac])
            print("Bulunmayan harfler: ", end="")
            for letter in kullanilan_harfler:
                if letter not in kelime:
                    print(letter, end=" ")
            print("")
        if sayac == 7:
            print("Hak bitti")
            break



