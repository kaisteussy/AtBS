import os
from pathlib import Path
import send2trash
import pyinputplus

p = Path(r'C:\Users\Bamboozle\PycharmProjects\automate_the_boring_stuff\Chapter 10\deleteUnneededFiles')

fileSize = 127000000
# fileSize = pyinputplus.inputInt(prompt='Please input file size in MB: ')

print(f'Checking for files larger than {fileSize} bytes...')

# Walk through path 'p', search for files greater than fileSize
for folderName, subfolders, files in os.walk(p):
    currentFolder = Path(folderName)

    for file in files:
        # Check for file size
        if os.path.getsize(currentFolder/file) >= fileSize:
            print(f'{os.path.getsize(currentFolder/file)} bytes {file} ')
            print(f'Deleting {currentFolder/file}')

            # Convert path to string and send to trash
            send2trash.send2trash(str(currentFolder/file))

