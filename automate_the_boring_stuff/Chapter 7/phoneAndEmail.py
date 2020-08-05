import pyperclip
import re

matchPhone = re.compile(r'''(
                        (\d{3}|\(\d{3}\))   # area code
                        (\s|-|\.)           # separator
                        (\d{3})             # first 3 digits
                        (\s|-|\.)           # separator
                        (\d{4})             # last 4 digits
                        (\s*(ext|x|ext.)\s*(\d{2,5}))? #extension
                        )''', re.VERBOSE)

matchEmail = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+    # address
                        @[a-zA-Z0-9.-]+      # domain name
                        \.(\w*)              # domain suffix
                        )''', re.VERBOSE)

matchURL = re.compile(r'''(
                      (http://|https://)   # prefix
                      (.*)                 # domain name
                      (\.\w{2,})           # suffix
                      )''', re.VERBOSE)

text = pyperclip.paste()

matches = []

for match in matchPhone.findall(text):
    phoneNum = '-'.join([match[1], match[3], match[5]])
    if match[8] != '':
        phoneNum += ' x' + match[8]
    matches.append(phoneNum)

for match in matchEmail.findall(text):
    matches.append(match[0])

for match in matchURL.findall(text):
    matches.append(match[0])

print('\n'.join(matches))
pyperclip.copy('\n'.join(matches))
