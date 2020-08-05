#! python3
# Usage: python text_files_to_spreadsheet.py <directory to read files from>

import openpyxl
import sys
import os
from pathlib import Path

# If a directory is specified, store in variable
if len(sys.argv) > 1:
    directory = sys.argv[1]
elif len(sys.argv) == 1:
    directory = ''

# Create a Path object as a working directory
currentDir = Path(os.path.abspath(os.curdir))
p = currentDir / directory
print('Reading contents from ' + str(p) + '...')

# Create the workbook object to output to
wb = openpyxl.Workbook()
sheet = wb.active

# Enumerate and loop through all text files in the directory
for column, file in enumerate(p.glob('*.txt')):
    # Open text file
    with open(file) as f:
        # Store lines in text file as a list
        lines = f.readlines()
        # Loop through and enumerate the list
        for row, line in enumerate(lines):
            sheet.cell(row=row+1, column=column+1).value = line


wb.save('output.xlsx')
wb.close()
