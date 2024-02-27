from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self,driver,email,password):
        self.driver = driver
        self.email = email
        self.password = password
    
    def login(self):
        self.driver.get("https://portal.naanmudhalvan.tn.gov.in/login")
        time.sleep(3)

        # username
        username_input = self.driver.find_element(By.NAME, "username")
        username_input.clear()
        username_input.send_keys(self.email)

        #password
        password_input = self.driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(self.password)

        # Click Captcha
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Please enter the characters on image']"))
        )
        input_field.click()

        # time to fill captcha
        time.sleep(20)

        # hack to go to mandiatory course 
        self.driver.get("https://portal.naanmudhalvan.tn.gov.in/mandatory/courses")
        
        # click the watch button 
        watch_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//td//button[contains(text(), 'Watch')]"))
        )
        watch_button.click()

        # click access course
        button_xpath = "//button[contains(@class, 'text-naan-success') and contains(@class, 'bg-naan-success-light')]"
        access_course = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_xpath))
        )

        # Click the button
        access_course.click()

        