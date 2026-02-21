"""

how to do it?
- get the flags to do specific things in the program (done)

- get the words you want to change as a parameter

- get the new file with a text you want to change some specific
words

- with the words you want to change, fetch for them in the text

- when you find the word to change, put another thing/word in that
place

- after all changes, create a new file and output that in the screen

"""


import sys

list_flags = list()
list_flags = sys.argv[0:]

for each in list_flags:
    if '-' in each:
        print(f"this thing is a flag: {each}\n")


print(f"this is the things you pass to the program:\n{sys.argv}")
