'''Generate funny nicknames similar to the TV show Psych'''

import random
import colorama as c
from names import first, last

c.init()


def nick_name():
    '''
    Function to generate nicknames based on user request
    '''

    return random.choice(first) + ' ' + random.choice(last)

print("Welcome to the Psych 'Sidekick Name Picker.'\n")

def main():
    '''Let user ask for nicknames until they find a good one'''

    while True:
        req = input('Would you like a nickname? (y or n) ')

        if req == 'y':
            print(f'{c.Fore.GREEN}Your new name is: {nick_name()}{c.Style.RESET_ALL}' + '\n')
        elif req == 'n':
            print('Thanks for playing. Have a nice day!')
            break
        else:
            print('Invalid input. Please enter y or n.')


# pylint output: first score not good. 4.12/10
# >pylint main.py
# ************* Module main
# main.py:25:0: C0304: Final newline missing (missing-final-newline)
# main.py:1:0: C0111: Missing module docstring (missing-docstring)
# main.py:8:0: C0111: Missing function docstring (missing-docstring)
# main.py:13:4: C0103: Constant name "req" doesn't conform to UPPER_CASE naming style (invalid-name)
# main.py:25:4: E0602: Undefined variable 'main' (undefined-variable)
# main.py:2:0: C0411: standard import "import random" should be placed before
# "import colorama as c" (wrong-import-order)

# -----------------------------------
# Your code has been rated at 4.12/10

# After refactor
# >pylint nickname.py

# -------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 9.44/10, +0.56)

if __name__ == '__main__':
    main()
