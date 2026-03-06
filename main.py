import sys
import os


sys.argv = sys.argv[1:] # taking off the program name
list_flags = list() # creating the list that will have all the flags
text_paths = list() # creating a list to save the path files
list_words_chng = list_words_put = "" # first is WORDS YOU WANT TO CHANGE second is WORDS TO BE THERE
lines = list() # for file lines
words = list() # for words of each line

def change(word_here, word_there):
    
    for text in sys.argv: # catching the files (in paths)
        if os.path.isfile(text) == True:
            text_paths.append(text)

    with open("/home/samuel/coding/testing/text.txt", 'r') as texto:
        lines = texto.readlines()

    with open("/home/samuel/coding/testing/text.txt", 'w') as texto: # getting each line of the text and spliting it into words list
        for index, each_line in enumerate(lines):
            # in each line remove: \n
            # in each line replace the word you don't want for the word you want
            lines[index] = each_line.lower().replace( word_here.lower(), word_there )
            texto.writelines(lines)


for each in sys.argv: # catching the flags 
    if '-' == each[0]:
        list_flags.append(each)

list_words_put = sys.argv[-2] # catching the almost last thing passed, the words to be there, in the place of words you don't want
list_words_chng = sys.argv[-1] # catching the last sentence passed and spliting the words in the string passed

# doing something for each type of flag
if len(list_flags) > 0:
    for each_flag in list_flags:
        if each_flag == '-u': # when you want an uppaer case character
            change(list_words_chng, list_words_put.upper())
        elif each_flag == '-l': # lower case words
            change(list_words_chng, list_words_put.lower())
        elif each_flag == '-c': # Capitalize the words that is going to be there
            change(list_words_chng, list_words_put.capitalize())
        
        
else:
    change(list_words_chng, list_words_put)
