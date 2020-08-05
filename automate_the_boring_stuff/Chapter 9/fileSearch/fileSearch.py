#! python3
# fileSearch.py - Takes in a regular expression as input. Searches all files in the directory for a match and
#                 outputs line matched to terminal.
# Usage: py.exe fileSearch.py <regular expression>

import re
from pathlib import Path
import sys

if len(sys.argv) == 2:
    match = re.compile(sys.argv[1])
else:
    match = re.compile(input('Please enter a regular expression: \n'))

p = Path.cwd()

for item in p.glob('*.txt'):
    file = open(f'{item}', 'r')
    line_count = 1
    for line in file.readlines():
        if match.search(line):
            print(f'Match found in {item.name} on line {line_count}')
            print(line)
        line_count += 1
    file.close()
