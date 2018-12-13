# Vigenere Cipher (Polyalphabetic Substitution Cipher)
# http://inventwithpython.com/hacking (BSD Licensed)
import pyperclip #This module is needed in order to automatically copy the text to clipboard

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    print("Welcome to the Python Vigenere Cipher Program!")

    while True:
        myMode = input(str("Please enter whether you wish to encrypt or decrypt a message!"))
        if myMode[0].lower() == "e":
            myMode = "encrypt"
            break
        elif myMode[0].lower() == "d":
            myMode = "decrypt"
            break
        else:
            print("Please choose either to encrypt or decrypt your message")
            continue #For some reason if I get the answer wrong it repeats line 19 over and over again

    myMessage = input(str("Please enter the message that you wish to encrypt/decrypt"))
    myKey = input(str("Please enter the key for encrypting/decrypting your message"))

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)

    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message has been copied to the clipboard.')
    again()


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] # stores the encrypted/decrypted message string

    keyIndex = 0
    key = key.upper()

    for symbol in message: # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) # add if encrypting
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex]) # subtract if decrypting

            num %= len(LETTERS) # handle the potential wrap-around

            # add the encrypted/decrypted symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            keyIndex += 1 # move to the next letter in the key
            if keyIndex == len(key):
                keyIndex = 0
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)

def again():
    while True:
        answer = input("Do you want to encryt/decrypt again? ")
        if answer[0].lower() == "y":
            playGame()
        elif answer == '':
            print("You know you need to type something, right?")

        else:
            print("Goodbye")
            break

# If vigenereCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()