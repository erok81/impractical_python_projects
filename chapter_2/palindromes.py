'Chapter Two - Palindromes'
import sys


def load_file():
    '''Loads file from disk'''
    try:
        with open('words.txt', 'r') as file:
            texts = file.read().split('\n')

            print('Load succesful')

            return texts

    except IOError as err:
        print(f'{err} opening words.txt. Program terminating')
        sys.exit(1)


def main():
    '''Main program'''
    dictionary = load_file()
    palindromes = []
    total = len(dictionary)
    counter = 0
    for word in dictionary:
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)
            counter += 1
        else:
            continue

    print(f'Out of {total} words, there are {counter} palindromes in the file. Here they are: \n')
    print(*palindromes, sep='\n')


if __name__ == "__main__":
    main()
