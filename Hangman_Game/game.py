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
kelimedekiHarfler = list(kelime)
dogruHarfler = []
kullanilan_harfler = []
sayac = 0
while (True):
    for element in kelime:
        if element in kullanilan_harfler:
            print(element, end=" ")
        elif element == " ":
            print("/ ", end="")
        else:
            print("_ ", end="")
    yeniHarf = input(" ")
    if dogruHarfler == kelimedekiHarfler:
        print(kelime)
        print("Kazandınız.")
    if yeniHarf in kullanilan_harfler:
        print("Harf daha önce girildi")
    else:
        kullanilan_harfler.append(yeniHarf)
        if yeniHarf not in kelime:
            sayac += 1
            if (sayac < 6):
                print(hangman[sayac])
                print("Bulunmayan harfler: ", end="")
                for letter in kullanilan_harfler:
                    if letter not in kelime:
                        print(letter, end=" ")
                print("")
            if sayac == 6:
                print(hangman[6])
                print("Hak bitti")
                break
        else:
            dogruHarfler.append(yeniHarf)
            if dogruHarfler == kelimedekiHarfler:
                print(kelime)
                print("Kazandınız.")
                break


