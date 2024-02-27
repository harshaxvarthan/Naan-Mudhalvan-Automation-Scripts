from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from login import LoginPage
from scrapper import Scrapper
import time

# Initialize the driver
driver = webdriver.Edge()
    
# Initialize the Pages
login_page = LoginPage(driver,"au112821104031","859993")
login_page.login()

# Automate
automate = Scrapper(driver)
automate.automate()
time.sleep(10)