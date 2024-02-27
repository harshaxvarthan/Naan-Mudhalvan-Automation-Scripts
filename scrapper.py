from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Scrapper:
    def __init__(self,driver):
        self.driver = driver
    
    def clickActivity(self):
        activity_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "video-activity-tab"))
        )
        activity_link.click()

    def clickViewAll(self):
        view_all_questions_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "view-all-questions"))
        )
        view_all_questions_button.click()

    def questionList(self):
        self.clickViewAll()
        # Wait for the Questions to be present
        questions= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'videoQuestionTabsContent')))
        question_list = questions.find_elements(By.CSS_SELECTOR, '#videoQuestionTabsContent .list-unstyled.questions-list li')
            
        # Wait for the first question to be clickable
        first_question = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.questions-list li:first-child'))
        )
        # Click the first element
        first_question.click()
        return question_list

    def options(self, q):
        # Wait for the options container to be present
        options_container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'.option-buttons[class*="{q}"]'))
        )
        option_buttons = options_container.find_elements(By.CLASS_NAME, 'options')
        return option_buttons

    def clickClose(self):
        # Wait for the button to be present, adjust timeout if needed
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'close')))
            # Find the button by class name and click it
            print('handling exception')
            close_button = self.driver.find_element(By.CLASS_NAME, 'close')
            close_button.click()

    def clickOption(self,options,which):
        self.driver.execute_script("arguments[0].click();", options[which])

    def submit(self):
        submit = WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.ID, 'submitbutton'))
        )
        submit.click()

    def click_next_button(self, parent_id):
        xpath = f'//button[@class="btn btn-primary nextbutton" and @data-parent="{parent_id}"]'
        next_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        next_button.click()
    def clickNext(self, parent_id):
        try:
            self.click_next_button(parent_id)
        except Exception as e:
            print('exception handling')
            self.submit()

    def answer(self,q,which,total):
        options=self.options(q) #calculates number of options
        self.clickOption(options,which) #clicks a option

        if(q==total):
            time.sleep(1)
            self.submit()
            print('submitted')
            return
        print('trying to click next')
        parent_id = f"#q{q}VideoActivity"
        self.clickNext(parent_id)
        print('next!')
        
    def resultx(self):
        try:
            # Find all elements with the class 'has-error'
            wrong_elements = WebDriverWait(self.driver, 5).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#questions-all .has-error'))
            )
            # Iterate through the wrong elements and perform any desired actions
            wrong_questions = []
            for wrong_element in wrong_elements:
                wrong_questions.append(int(wrong_element.text))  # or do something else with the wrong elements
            wrong_elements[0].click()
            return wrong_questions
        except Exception as e:
            print('exception handling')
            time.sleep(3)
            try:
                print('trying to close')
                self.clickClose()
            except Exception as e:
                print('completed closing failed ')
                
            wrong_questions = []
            return wrong_questions
    
    def completeClick(self):
        # Adjust the timeout and other conditions as necessary
        wait = WebDriverWait(self.driver, 4)
        button = wait.until(EC.element_to_be_clickable((By.ID, "loadNextLesson")))

        # Click the button
        button.click()

    def wrongFix(self,wrong_questions,total,which):
        if not wrong_questions:
            print("List is empty. Recursion terminated.")
            return
        
        q = wrong_questions[0]
        for x in range(wrong_questions[0],total+1):
            if x in wrong_questions:
                self.answer(q,which,total)
                q+=1
                print(x,'question incorrect so fixing')
            else:
                if(x==total):
                    time.sleep(1)
                    self.submit()
                    break
                print(x,'question correct so skipping')
                parent_id = f"#q{q}VideoActivity"
                self.clickNext(parent_id)
                q+=1
        time.sleep(2)
        wrong_questions=self.resultx()
        self.wrongFix(wrong_questions,total,which+1)

    def automate(self):
        print('in')
        self.clickActivity()
        question_list = self.questionList()
        total=int(len(question_list)/2)
        
        q = 1
        which = 0
        for x in range(total):
            self.answer(q,which,total)
            q +=1
        time.sleep(1)
        wrong_questions=self.resultx()
        self.wrongFix(wrong_questions,total,which+1)