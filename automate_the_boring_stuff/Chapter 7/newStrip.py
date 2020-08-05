import re

string = input("Enter a string to strip: ")
bad_chars = input("Enter the characters you want to be striped: ")


def regex_strip(s, chars=r'\s'):
    char_cls = build_re_character_class(chars)
    return re.sub(r'^' + char_cls + r'*(.*?)' + char_cls + r'*$', r'\1', s)


def build_re_character_class(chars):
    return r'[' + re.sub(r'([\]\\\^\-])', r'\\\1', chars) + r']'


try:
    print(regex_strip(string, bad_chars))
except TypeError:
    print(regex_strip(string, ' '))