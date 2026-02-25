"""

how to do it?
- get the flags to do specific things in the program (done)

- get the words you want to change as a parameter (done)

- get the new file with a text you want to change some specific
words (get the words you wanto to change, that words should be between -> "") (done)

- with the words you want to change, fetch for them in the text
get words:
    catch each line of the text
    split all words in a list
    fetch for the words you want to change

when found:



- when you find the word to change, put another thing/word in that
place

- after all changes, create a new file and output that in the screen

##################################################################
syntax of the command:  chwd  -flags  complete_paths_to_files  words_you_wanna_change


"""


import sys
import os

sys.argv = sys.argv[1:] # taking off the program name
list_flags = list() # creating the list that will have all the flags
list_words_chg = list() # saving the words to change
text_paths = list() # creating a list to save the path files
list_words_txt = list() # list of words in each line of the text


for each in sys.argv: # catching the flags 
    if '-' == each[0]:
        list_flags.append(each)


for text in sys.argv: # catching the files (in paths)
    if os.path.isfile(text) == True:
        text_paths.append(text)


list_words_chg = sys.argv[-1].split() # catching the last sentence passed and spliting the words in the string passed


with open("/home/samuel/coding/testing/text.txt") as texto: # getting each line of the text and spliting it into words list
    for lines in texto:
        """ remove the \n from the text """
        list_words_txt.append(lines.replace("\n", "").split(' '))


for number, words in enumerate(list_words_txt): # testing
    print("{} - {}".format(number, words))
    if number == 6: break
