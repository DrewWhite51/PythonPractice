# Shows how sys.exit() exits out of the program
import sys

while True:
    print('Type exit to exit.')
    response = input('')
    if response == 'exit':
        sys.exit()
    print('You typed  ' + response + '.')

    