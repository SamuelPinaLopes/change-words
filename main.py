"""

how to do it?
- get the flags to do specific things in the program (done)

- get the words you want to change as a parameter (done)

- get the new file with a text you want to change some specific
words (get the words you wanto to change, that words should be between -> "") (done)

- with the words you want to change, fetch for them in the text

- when you find the word to change, put another thing/word in that
place

- after all changes, create a new file and output that in the screen

##################################################################
syntax of the command:  chwd  -flags  complete_paths_to_files  words_to_change_to  words_you_wanna_change


# Read all lines
with open("file.txt", "r") as file:
    lines = file.readlines()

# Modify specific line (e.g., line 2, index 1)
lines[1] = "New content here\n"

# Write back to file
with open("file.txt", "w") as file:
    file.writelines(lines)


"""


import sys
import os

sys.argv = sys.argv[1:] # taking off the program name
list_flags = list() # creating the list that will have all the flags
text_paths = list() # creating a list to save the path files
list_words_chng = list_words_put = "" # saving the words to change # list of words to substituite the ones already there
lines = list() # for file lines
words = list() # for words of each line


for each in sys.argv: # catching the flags 
    if '-' == each[0]:
        list_flags.append(each)


for text in sys.argv: # catching the files (in paths)
    if os.path.isfile(text) == True:
        text_paths.append(text)

list_words_put = sys.argv[-2] # catching the almost last thing passed, the words to be there, in the place of words you don't want


list_words_chng = sys.argv[-1] # catching the last sentence passed and spliting the words in the string passed

with open("/home/samuel/coding/testing/text.txt", 'r') as texto:
    lines = texto.readlines()

with open("/home/samuel/coding/testing/text.txt", 'w') as texto: # getting each line of the text and spliting it into words list

    for index, each_line in enumerate(lines):
        # in each line remove: \n
        # in each line replace the word you don't want for the word you want
        lines[index] = each_line.lower().replace( list_words_chng.lower(), list_words_put.lower() )
    
    texto.writelines(lines)
