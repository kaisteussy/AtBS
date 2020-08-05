#! python3
# madLibs.py - Reads a text file, looks for ADJECTIVE, NOUN, ADVERB, or VERB. Prompts user to replace each.
#              Prints results to screen and saves to newText.txt.
# Usage: py.exe madLibs.pyw <file.txt>

import sys, re

file = open(f'{sys.argv[1]}', 'r')

text = '\n'.join(file.readlines())
file.close()
text = text.split()

for i in range(len(text)):
    if re.search(r'ADJECTIVE', text[i]):
        text[i] = text[i].replace('ADJECTIVE', input('Please enter an adjective:\n'))
    if re.search(r'VERB', text[i]):
        text[i] = text[i].replace('VERB', input('Please enter a verb:\n'))
    if re.search(r'NOUN', text[i]):
        text[i] = text[i].replace('NOUN', input('Please enter a noun:\n'))

text = ' '.join(text)
print(text)

newFile = open('newText.txt', 'w')
newFile.write(text)
newFile.close()
