'''Practice project from chapter one. Making a poor man's bar chart'''
import pprint

text = input('Enter a sentence you\'d like to plot \n')

letter_dict = {'a': [],
               'b': [],
               'c': [],
               'd': [],
               'e': [],
               'f': [],
               'g': [],
               'h': [],
               'i': [],
               'j': [],
               'k': [],
               'l': [],
               'm': [],
               'n': [],
               'o': [],
               'p': [],
               'q': [],
               'r': [],
               's': [],
               't': [],
               'u': [],
               'v': [],
               'w': [],
               'x': [],
               'y': [],
               'z': [],
}

for letter in text:
    if letter in [',', ' ', '.', '?']:
        pass
    else:
        letter_dict[letter].append(letter)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(letter_dict)