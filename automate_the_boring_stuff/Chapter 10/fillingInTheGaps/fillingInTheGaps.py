#! python3
# fillingInTheGaps.py - Renames any files that are out of sequence

from pathlib import Path
import re
import os

p = Path(r'C:/Users/Bamboozle/PycharmProjects/learning_material/Chapter 10/fillingInTheGaps/filesWithGaps')
match = re.compile(r'^(spam)(\d{3})(\.txt)$')

count = 0

# Get ONLY files (not directories) in the directory and add them to the list 'files'
files = [item.name for item in os.scandir(p) if item.is_file()]

# Enumerate files list and rename using regex groups, os.rename(), and .zfill() method only.
for index, item in enumerate(files):
    fileMatch = re.match(match, item)
    file_index = str(index + 1).zfill(int(3))
    newName = fileMatch.group(1) + file_index + fileMatch.group(3)
    if newName != item:
        print(f'{item} out of sequence, renaming to {newName}...')
        os.rename(p/item, p/newName)
        print('Done')


