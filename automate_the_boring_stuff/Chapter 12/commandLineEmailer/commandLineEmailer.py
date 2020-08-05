#! python3
# commandLineEmailer.py

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyip
import time

# Username and password to login
username = pyip.inputStr('Enter your ProtonMail username: ')
password = pyip.inputStr('Enter your password: ')
destinationEmail = pyip.inputStr('Enter the address to send your Email to: ')

# Set browser to Chrome and open ProtonMail
print('Opening ProtonMail with Chrome...')
browser = webdriver.Chrome()
browser.get('https://protonmail.com')

# Find login button by CSS selector
login = browser.find_element_by_css_selector('#bs-example-navbar-collapse-1 > ul > li:nth-child(7) > a')
login.click()

# Fill out username and password fields, click Login
print('Logging in...')
usernameField = browser.find_element_by_id('username')
usernameField.send_keys(username)
passwordField = browser.find_element_by_id('password')
passwordField.send_keys(password)
loginButton = browser.find_element_by_id('login_btn')
loginButton.click()

# Wait 5 seconds for page to load
time.sleep(5)

# Compose new email
composeButton = browser.find_element_by_css_selector('#pm_sidebar > button')
composeButton.click()
time.sleep(2) # Sleep 2 seconds for iframe to open


# Fill in 'To' field and press enter to accept form submit
toField = browser.find_element_by_name('autocomplete')
toField.send_keys(destinationEmail, Keys.ENTER)


# Fill 'Subject' field via XPATH (all other selection methods unviable due to variable elements within iframe)
subjectField = browser.find_element_by_xpath('/html/body/div[2]/form[1]/div/div[2]/div[5]/input')
subjectField.send_keys('This is a test!')


# Fill out body of email via XPATH (all other selection methods unviable due to variable elements within iframe)
emailBody = browser.find_element_by_xpath('/html/body/div[2]/form[1]/div/section/div/div[3]/div[2]/div[2]/iframe')
emailBody.send_keys('This is a test!')

# Click send button and wait 4 seconds for email to send
print('Sending...')
sendButton = browser.find_element_by_xpath('/html/body/div[2]/form[1]/div/footer/div/button[3]')
sendButton.click()
time.sleep(4)


# Close browser.
print('Closing browser...')
browser.close()
