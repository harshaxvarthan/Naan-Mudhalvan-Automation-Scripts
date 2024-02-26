"""
This is simple Naan Mudhalvan Automation Script to complete the quiz seelction of the Neural Networks Course
This is a WIP Script which will not be actively maintained 
People who are intersted to contribute to the Project can Fork and submit Pull Requests
Author: harshaxvarthan
"""
from selenium import webdriver
import login
import time

driver = webdriver.Edge()
login.login(driver)




driver.close()