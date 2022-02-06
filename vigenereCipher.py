"""
Russell Deady
Program I made to use the vigenere cipher encryption method
"""

def main():

    plainText = ""
    cipherText = ""
    shiftKey = ""
    
    print()
    print("Welcome to the vigenere cipher encryptor!")
    plainText = input("Enter a message to encrypt: ")
    shiftKey = input("Enter a key to use for the encryption: ")

    i = 0
    while i <= len(plainText) - 1:
        uniCodeValue = ord(plainText[i])
        sizeOfShift = ord(shiftKey[i % len(shiftKey)])
        if (sizeOfShift < 91):
            sizeOfShift -= 65
        else:
            sizeOfShift -= 97

        if (plainText[i] == " "):
            cipherText = cipherText + " "
            i += 1
            continue
        elif (plainText[i].isalpha() == False):
            cipherText = cipherText + plainText[i]
            i += 1
            continue

        if (uniCodeValue < 91):
            uniCodeValue = uniCodeValue + int(sizeOfShift) % 26
            if (uniCodeValue > 90):
                uniCodeValue -= 26
        else: 
            uniCodeValue= uniCodeValue + int(sizeOfShift) % 26
            if (uniCodeValue >= 123):
                uniCodeValue -= 26
        newChar = chr(uniCodeValue)
        cipherText = cipherText + newChar

        i += 1

    print()
    print("Your encrypted message is...")
    print(cipherText)
    print()
    print("Thank you for using the encryptor!")
    print()

main()
