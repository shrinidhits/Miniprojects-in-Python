morse_code = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
def encryption(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += morse_code[letter] + ' '
        else:
            cipher += ' '
    return cipher

def decryption(message):
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(morse_code.keys())[list(morse_code
                                                              .values()).index(citext)]
                citext = ''
    return decipher




def main():
    print("Enter your message to be converted to Morse Code")
    message = input()
    result = encryption(message.upper())
    print("\nMorse code of your message is:")
    print (result)
    message = result
    result = decryption(message)
    print("\n\nConverting this back to original message")
    print (result)
if __name__ == '__main__':
    main()

