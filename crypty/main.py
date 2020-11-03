"""
Encryption/Decryption of messages in either International Morse Code or Binary.

Attributes:
    morse_code_dict: (dict) A dictionary of letters and numbers to morse code.
    binary_dict: (dict) A dictionary of letters and symbols to binary.
    retry_message: (str) A message to prompt the user to retry if their message in invalid.
    end_message: (str) A message that indicates that no more prompts will be given.

Functions:
    morse: Prompts the user for a message and then encrypts/decrypts it depending on the input.
    binary: Prompts the user for a message and then encrypts/decrypts it depending on the input.
    morbin: Contains all the code for morse and binary; can be used instead of them.
    encrypt: Encrypts a message.
    decrypt: Decrypts a message.
"""


morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                   'Y': '-.--', 'Z': '--..',

                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.', '0': '-----'}

binary_dict = {'A': '01000001', 'B': '01000010', 'C': '01000011', 'D': '01000100', 'E': '01000101', 'F': '01000110',
               'G': '01000111', 'H': '01001000', 'I': '01001001', 'J': '01001010', 'K': '01001011', 'L': '01001100',
               'M': '01001101', 'N': '01001110', 'O': '01001111', 'P': '01010000', 'Q': '01010001', 'R': '01010010',
               'S': '01010011', 'T': '01010100', 'U': '01010101', 'V': '01010110', 'W': '01010111', 'X': '01011000',
               'Y': '01011001', 'Z': '01011010',

               'a': '01100001', 'b': '01100010', 'c': '01100011', 'd': '01100100', 'e': '01100101', 'f': '01100110',
               'g': '01100111', 'h': '01101000', 'i': '01101001', 'j': '01101010', 'k': '01101011', 'l': '01101100',
               'm': '01101101', 'n': '01101110', 'o': '01101111', 'p': '01110000', 'q': '01110001', 'r': '01110010',
               's': '01110011', 't': '01110100', 'u': '01110101', 'v': '01110110', 'w': '01110111', 'x': '01111000',
               'y': '01111001', 'z': '01111010',

               '.': '00101110', ',': '00100111', '!': '00100001', '"': '00100010', '#': '00100011', '$': '00100100',
               '%': '00100101', '&': '00100110', "'": '00100111', '(': '00101000', ')': '00101001', '*': '00101010',
               '+': '00101011', '-': '00101101', '/': '00101111', '?': '00111111', '@': '01000000', '_': '01011111'}

retry_message = "\nInvalid Message. Try Another."
end_message = "\nToo Many Invalid Messages.\n"


def encrypt(message, dictionary):
    """ Encrypts a message.

    :param message: (str) The message to encrypt.
    :param dictionary: (dict) The desired dictionary.
    :return: (str) The encrypted message.
    """

    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += dictionary[letter] + ' '
        else:
            cipher += '   '
    return cipher


def decrypt(message, dictionary):
    """ Decrypts a message.

    :param message: (str) The message to decrypt.
    :param dictionary: (dict) The desired dictionary.
    :return: (str) The decrypted message.
    """

    message += ' '
    decipher = ''
    citext = ''
    for symbol in message:
        if symbol != ' ':
            i = 0
            citext += symbol
        else:
            i += 1
            if i == 2:
                decipher += ' '
            else:
                decipher += list(dictionary.keys())[list(dictionary.values()).index(citext)]
                citext = ''
    return decipher


def morbin(switch, message_test=None):
    """ Prompts the user for a message and then encrypts/decrypts it depending on the input.

    :param switch: (bool) If True will use morse code, and if False will use binary.
    :param message_test: (str or None) If given a string, will use as the input for testing purposes (default is None).
    :return: (str) Either the encrypted message, decrypted message, or the end_message variable.
    """

    if switch:
        dictionary = morse_code_dict
        char_list = ['.', '-']
    else:
        dictionary = binary_dict
        char_list = ['0', '1']

    counter = 1
    while counter <= 5:
        if message_test is None:
            message = input("What is your message?   ")
        else:
            message = message_test

        m = message.upper()
        if set(m).isdisjoint(dictionary.keys()) is False:
            if set(message).isdisjoint(char_list) is True:
                return encrypt(m, dictionary)
        else:
            if set(message).isdisjoint(char_list) is False:
                return decrypt(m, dictionary)

        counter += 1
        if counter < 5:
            print(retry_message)
        else:
            print(end_message)
            return end_message


def morse():
    """ Prompts the user for a message and then encrypts/decrypts it depending on the input.

    :return: The encrypted/decrypted message.
    """

    m = morbin(switch=True)
    print(m)
    return m


def binary():
    """ Prompts the user for a message and then encrypts/decrypts it depending on the input.

    :return: The encrypted/decrypted message.
    """

    m = morbin(switch=False)
    print(m)
    return m
