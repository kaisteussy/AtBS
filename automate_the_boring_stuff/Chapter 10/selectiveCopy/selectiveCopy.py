from pathlib import Path
import os
import shutil
import re
import pyinputplus


print('Hello, welcome to selectiveCopy. ')

fileType = re.compile(r'^\..+')

# Input an extension that matches a '.' followed by one or more characters.
extension = pyinputplus.inputRegex(fileType, prompt='Please input the filetype you would like to copy, (e.g.: .txt): ')

# Show current directory and all subfolders
print(f'Current directory: {Path.cwd()}')
print('Folders:')
[print(f.path) for f in os.scandir(Path.cwd()) if f.is_dir()]

# Input the source file path. This path MUST exist.
sourceFolder = Path(pyinputplus.inputFilepath(prompt='Please enter which source folder you would like to copy from: ', mustExist=True))

# Input the destination file path. This path does NOT need to exist.
destinationFolder = Path(pyinputplus.inputFilepath(prompt='Please enter the destination folder: ', mustExist=True))
print()


print(f'Starting search for all files ending in {extension} in {sourceFolder}...')
print()
# Walk the sourceFolder directory and copy all files that match the file extension to destinationFolder.
for folderName, subfolders, filenames in os.walk(sourceFolder):
    currentFolder = Path(folderName)
    print(f'Scanning {currentFolder}...')

    for filename in filenames:
        if filename.endswith(extension):
            print(f'Found match: {currentFolder / filename}')
            print(f'Copying {os.path.abspath(currentFolder/filename)} to \{destinationFolder}...')
            # shutil.copy(currentFolder/filename, destinationFolder)

    print('\n')

