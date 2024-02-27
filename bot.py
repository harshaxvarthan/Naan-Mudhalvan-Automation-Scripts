from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from login import LoginPage
from scrapper import Scrapper
from topic_scrapper import TopicScrapper
import time
import os

import os

module = int(input('Enter the Module Number '))


def save_credentials(credentials, filename):
    with open(filename, "w") as file:
        file.write(credentials)

def load_credentials(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    return None

# Check if the username/password credentials file exists
username_password_credentials_file = "username_password_credentials.txt"
username_password_saved_credentials = load_credentials(username_password_credentials_file)

# Use saved username/password credentials if available
if username_password_saved_credentials:
    print(f"Using saved username/password credentials: {username_password_saved_credentials}")
    # Extract username and password if needed
    username = username_password_saved_credentials.split(":")[1].strip().split(",")[0].strip()
    password = username_password_saved_credentials.split(":")[2].strip()
# If no saved credentials, prompt the user for login
else:
    login = int(input("""
    How do you want to login?
    '1' Mobile Phone (limit 3)
    '2' Username/Password (Recommended)
    """))

    if login == 1:
        phone = int(input("Enter the mobile number: "))

    elif login == 2:
        username = str(input("Enter the username: "))
        password = str(input("Enter the password: "))
        username_password_credentials = f"Username: {username}, Password: {password}"
        save_credentials(username_password_credentials, username_password_credentials_file)
        print(f"Login details have been saved to '{username_password_credentials_file}'")


# Initialize the driver
driver = webdriver.Edge()
    
# Initialize the Pages
login_page = LoginPage(driver,username,password)
login_page.login()

# Automate
automate = Scrapper(driver)

# Scrap topics
topic = TopicScrapper(driver)
topic.automate(module)
time.sleep(10)
