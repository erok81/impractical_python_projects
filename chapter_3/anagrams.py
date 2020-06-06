'''Chapter 3 Anagrams'''
import sys

def load_file():
    '''Loads file from disk'''
    try:
        with open('../chapter_2/words.txt', 'r') as file:
            texts = file.read().split('\n')

            #print('Load succesful')

            return texts

    except IOError as err:
        print(f'{err} opening words.txt. Program terminating')
        sys.exit(1)

def main(user_word):
    '''main program'''
    words = load_file()
    anagrams = []
    for word in words:
        if len(user_word) == len(word) and sorted(list(word)) == sorted(list(user_word)):
            anagrams.append(word)

    return anagrams


if __name__ == "__main__":
    WORD = input('Enter anagram word: \n')
    WORD = WORD.upper()

    ANAGRAMS = main(WORD)

    print(f'Here are the anagrams for {WORD}')
    print(', '.join(ANAGRAMS))
