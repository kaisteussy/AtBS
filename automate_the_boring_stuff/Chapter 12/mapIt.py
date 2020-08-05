#! python3

import sys
import webbrowser
import pyperclip

if len(sys.argv) > 1:
    # Get address form command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address form clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
