import re
import pyperclip
import datetime

DATESLIST = []
VALIDDATES = []
matchDATES = re.compile(r'''(
                            ([0-2]\d|30|31)                             # Day
                            (-|/|.)                                     # Separator
                            (0\d|1[0-2])                                # Month
                            (-|/|.)                                     # Separator
                            (19\d\d|20\d\d)                             # Year
                            )''', re.VERBOSE)

# copies the contents of the clipboard to a variable
text = pyperclip.paste()

# test string
# text = '''
# 29/08/2012
# 31/12/2020
# 31/02/2020
# 31/04/2021'''

# attempts to create datetime objects from the contents of the clipboard
print('Processing dates...')
for match in matchDATES.findall(text):
    year, month, day = int(match[5]), int(match[3]), int(match[1])
    try:
        VALIDDATES.append(datetime.date(year, month, day))
    except ValueError:
        print(f'{match[0]} is not a valid date')
print()

print('Valid dates:')
for dt in VALIDDATES:
    print(dt)


