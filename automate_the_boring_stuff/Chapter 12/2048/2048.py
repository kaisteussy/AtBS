import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://play2048.co/')


game = browser.find_element_by_xpath('/html/body')

while True:
    game.send_keys(Keys.ARROW_UP)
    game.send_keys(Keys.ARROW_RIGHT)
    game.send_keys(Keys.ARROW_DOWN)
    game.send_keys(Keys.ARROW_LEFT)
    if game.find_element_by_xpath('/html/body/div[3]/div[4]/div[1]/p').text == 'Game over!':
        time.sleep(5)
        browser.close()


