def comma_code(lst):
    str = ''
    for item in lst:
        if item != lst[-1]:
            str += item + ', '
        else:
            str += 'and ' + item + '.'
    return str


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))
