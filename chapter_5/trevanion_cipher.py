''' THE OBJECTIVE:
    Write code that finds the letters hidden after punctuation marks in a null cipher and lets
    the user choose the number of letters after a punctuation mark to search for a solution.'''


import re
import colorama as c
c.init()
###### TEST MESSAGE ####
#Dear bean junky: it has come to my attention, like some of us,
#iguanas are green. keen to find out, everyone has started painting themselves green.
#because of this, everyone now smells like peas, animal dung, nd trousers. send help.
#######################

#####SECRET MESSAGE####
#i like beans
#######################


def main(message, num):
    '''Decode a null cipher message. Requires message and digit to check'''
    message = message.replace(' ', '')
    split = re.split('[,:?.!]', message)

    decoded = ''
    for word in split[1:]:
        try:
            decoded += word[num-1]
        except:
            pass

    return decoded

if __name__ == "__main__":

    MESSAGE = input('Enter a message to decode: \n')
    NUM = int(input('Now enter a digit to check: '))

    DECODED = main(MESSAGE, NUM)
    BORDER = len(DECODED)

    print('#'*(BORDER),'SECRET MESSAGE','#'*(BORDER))
    print(f'#{c.Fore.GREEN}{DECODED.center((BORDER*2)+14)}{c.Style.RESET_ALL}#')
    print('#' * ((BORDER * 2)+16))

