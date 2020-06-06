'''Encrypt a Civil War 'rail fence' type cipher.

    This is for a '2-rail' fence cipher for short messages.

    Example text to encrypt: 'Buy more Maine potatoes'
    
    Rail fence style: B Y O E A N P T T E
    
    U M R M I E O A O S
    
    Read zigzag: \/\/\/\/\/\/\/\/\/\/
    
    Encrypted: BYOEA NPTTE UMRMI EOSOS
'''
import math
import itertools


def main_encrypt():
    '''Run program to encrypt message using 2-rail rail fence cipher.'''
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)


def main_decrypt():
    '''Run decode program'''
    row1, row2 = split_rails(codetext)
    word = decrypt(row1, row2)
    return word


def prep_plaintext(plaintext):
    '''Remove spaces & leading/trailing whitespace.'''
    message = ''.join(plaintext.split())
    message = message.upper() # convention for ciphertext is uppercase
    print('\nplaintext = {}'.format(plaintext))
    return message


def build_rails(message):
    '''Build strings with every other letter in a message.'''
    evens = message[::2]
    odds = message[1::2]
    rails = evens + odds
    return rails


def encrypt(rails):
    '''Split letters in ciphertext into chunks of 5 & join to make string.'''
    ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
    print('ciphertext = {}'.format(ciphertext))


def split_rails(message):
    """Split message in two, always rounding UP for 1st row."""
    row_1_len = math.ceil(len(message)/2)
    row1 = (message[row_1_len:]).lower()
    row2 = (message[:row_1_len]).lower()
    return row1, row2

def decrypt(row1, row2):
    """Build list with every other letter in 2 strings & print."""
    plaintext = []
    for r1, r2 in itertools.zip_longest(row1, row2):
        plaintext.append(r1)
        plaintext.append(r2)
    if None in plaintext:
        plaintext.pop()
    print(f'rail 1 = {row1}')
    print(f'rail 2 = {row2}')
    print(f'\nplaintext = {"".join(plaintext)}')


if __name__ == '__main__':

 
    choice = input('Would you like to encode or decode?' )
    if choice == 'encode':
        plaintext = input('Please enter a message to encrypt: \n')
        main_encrypt()
    elif choice == 'decode':
        codetext = input('Please enter a message to decrypt: \n')
        main_decrypt()
    else:
        choice = input('Available choices are encrypt or decrypt')