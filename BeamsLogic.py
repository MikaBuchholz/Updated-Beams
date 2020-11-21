import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

class User:
    def __init__(self, email, password, message, teams_link, start_hour, startMinute = None):
        self.email = email
        self.password = password
        self.message = message
        self.teams_link = teams_link
        self.start_hour = start_hour
        self.startMinute = startMinute
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36 OPR/60.0.3255.170"}
        self.driver = webdriver.Firefox()

    def varSetup(self):
        link = self.teams_link
        page = requests.get(link, headers=self.headers)
        self.driver.get(self.teams_link)

    def loginManager(self):
        time.sleep(5)

        email_field = self.driver.find_element_by_id("i0116") 
        email_field.send_keys(self.email)

        time.sleep(2)
        next_button = self.driver.find_element_by_id("idSIButton9")
        next_button.click()
        
        password_field = self.driver.find_element_by_id("i0118")
        password_field.send_keys(self.password)
        time.sleep(6)
       
    def signInFieldInput(self):
        sign_in_button = self.driver.find_element_by_id("idSIButton9")
        sign_in_button.click()
        time.sleep(2)

    def yesPopUpClicker(self):
        yes_button = self.driver.find_element_by_id("idSIButton9")
        yes_button.click()
        time.sleep(5)
    
    def useWebVersion(self):
        webButton = self.driver.find_element_by_class_name("use-app-lnk")
        webButton.click()
        time.sleep(5)

    def startNewConvo(self):
        convoButton = self.driver.find_element_by_id("new-post-button")
        convoButton.click()
        time.sleep(5)

    def sendMessage(self):
        message_field = self.driver.find_element_by_class_name("cke_editable")
        message_field.send_keys(self.message)
        time.sleep(2)
        
    def dismissPopClicker(self):
        dismiss_pop_up_field = self.driver.find_element_by_class_name("text")
        dismiss_pop_up_field.click()
        time.sleep(5)
       
    def pressSendButton(self):
        send_button = self.driver.find_element_by_class_name("icons-send")
        send_button.click()
    
    def startFunction(self):
        loopstatus = True
        hours = self.start_hour

        while loopstatus:
            current_time = datetime.datetime.now()
        
            if hours == current_time.hour and self.startMinute == current_time.minute:
                loopstatus = False
                self.varSetup()
                self.loginManager()
                self.signInFieldInput()
                self.yesPopUpClicker()
                self.useWebVersion()
                self.startNewConvo()
                self.sendMessage()
                self.dismissPopClicker()
                self.pressSendButton()

