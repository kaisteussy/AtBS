#! python3
# Usage: python blank_row_inserter.py <row> <number of blank rows> <file.xlsx>

import openpyxl
import sys

# Get the command line arguments and store in variables
if len(sys.argv) == 4:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    file = sys.argv[3]

# Open the specified workbook and set the active sheet
wb = openpyxl.load_workbook(file)
sheet = wb.active

for _ in range(m):
    sheet.insert_rows(n)

wb.save('Edited-' + file)
wb.close()
