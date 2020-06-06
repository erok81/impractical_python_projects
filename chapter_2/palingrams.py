'Chapter Two - Palingrams'
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


def find_palingrams():
    '''Find dictionary palingrams'''
    pali_list = []
    word_list = load_file()
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    pali_list.append((rev_word[:end-i], word))
        
    return pali_list

print(find_palingrams())