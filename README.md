# **Naan Mudhalvan Automation Scripts**
*Author: harshaxvarthan*

**Overview**

This repository contains Selenium automation scripts for Naan Mudhalvan course (Neural Networks and Deep Learning - E2324)	
\
This script is designed to perform automated tasks for completing the activity quizzes
\
This is still in the alpha stage, and contributions are welcome
Do not expect support as this is just a hobby 
\
**Bugs**:
    1. You'll have to manually close the popup on www.guvi.in; do not touch anything else 
    2. Crashes unexpectedly

**Warning**
    1. Make sure you enter the correct module number you are currently in after the script crashes
    2. Do not touch/click anything
    3. Do not maximize/minimize the window; fix the typos in this code

## Setup

1. Clone the repository or download as a zip and extract:

    ```bash
    git clone https://github.com/your-username/naan-mudhalvan-automation.git
    ```
2. Install Dependencies by running setup.bat as an administrator

3. Set up Credentials inside credentials.txt:

    ```bash
    username = "YourUserName"
    password = "Password"
    phone = "YourNumber"
    ```
4. Start the bot:

    ```bash
    python bot.py
    ```
5. Enter the Module Number you are currently in
    ```
    Enter the Module Number: 1 //(1-5)
    ```
6. Select the login method 

    ```bash
    '1' -> Phone Number (max 3 tries)
    '2' -> login with username and password (recommended)
    ```
7. Enter the OTP or captcha within 30 seconds