import re

# checks for a password that is at least 8 characters long, one uppercase, one lowercase, one number
passwordLENGTH = re.compile(r'.{8,}')
passwordUPPERCASE = re.compile(r'[A-Z]+')
passwordLOWERCASE = re.compile(r'[a-z]+')
passwordDIGIT = re.compile(r'\d+')

password = 'i like ham'
password2 = 'Hello12345'
password3 = 'isthisStrongenough?'
password4 = '4WithLovefromAmy12'


def check_password_strength(pw):
    if not passwordLENGTH.search(pw):
        print('Must be 8 characters')
    if not passwordUPPERCASE.search(pw):
        print('Must have one uppercase letter')
    if not passwordLOWERCASE.search(pw):
        print('Must have one lowercase letter')
    if not passwordDIGIT.search(pw):
        print('Must include a number')


check_password_strength(password)
# check_password_strength(password2)
# check_password_strength(password3)
# check_password_strength(password4)


