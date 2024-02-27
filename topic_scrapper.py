from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from scrapper import Scrapper

modules = 5
class TopicScrapper:
    def __init__(self, driver):
        self.driver = driver
    
    def clickModule(self):
        # Wait for the modules to be present, adjust timeout if needed
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-link')))

        # Find all module buttons and click them iteratively
        module_buttons = self.driver.find_elements(By.CLASS_NAME, 'btn-link')
        return module_buttons

    def scrap(self, x):
        module_selector = f'modulel{x}'
        
        try:
            module_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, module_selector)))

            # Check if the module is visible
            if module_element.is_displayed():
                # Find all list items within the module
                topics = module_element.find_elements(By.CSS_SELECTOR, '.stepper li')
                


                # Iterate over the list items and print their text content
                for item in topics:
                    scrapper = Scrapper(self.driver)
                    try:
                        item.click()
                    except Exception as e:
                        scrapper.completeClick()
                    time.sleep(2)
                    scrapper.automate()
                    time.sleep(2)
            else:
                print('Module is not visible.')
        except Exception as e:
            print(e)

    def checkProgress(self):
        progress_bar = self.driver.find_elements(By.CLASS_NAME, "progress-bar")
        modules = 0
        for items in progress_bar:
            current_percentage = items.get_attribute("aria-valuenow")
            if (int(current_percentage.strip('%'))) == 0:
                return modules
            if (int(current_percentage.strip('%')))<=100:
                modules +=1
                continue
        return modules

    def automate(self):
        module_elements = self.clickModule()
        current_module = 5
        modules = self.checkProgress()
        loop = 1
        if(current_module>modules):
                current_module+=1
                module_elements[current_module-1].click()
        for x in range(current_module,6):
            if(loop !=1):
                scrapper = Scrapper(self.driver)
                try:
                    time.sleep(2)
                    module_elements[current_module-1].click()
                except Exception as e:
                    try:
                        time.sleep(2)
                        scrapper.clickClose()
                    except Exception as e:
                        scrapper.completeClick()
            time.sleep(2)
            self.scrap(current_module)
            time.sleep(2)
            current_module+=1
            loop +=1
            
            