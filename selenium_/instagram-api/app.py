import os
import time

from dotenv import load_dotenv, find_dotenv, dotenv_values
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv(".env")

class Instagram:
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.baseUrl="https://www.instagram.com/accounts/login/"

    def sign_in(self):
        self.browser.get(self.baseUrl)
        username_input=WebDriverWait(self.browser,3).until(lambda driver:driver.find_element(By.NAME,"username"))
        password_input=WebDriverWait(self.browser,3).until(lambda driver:driver.find_element(By.NAME,"password"))

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        element=WebDriverWait(self.browser,10).until(lambda driver:driver.find_elements(By.CLASS_NAME,"_acan"))
        element[1].click()
        element = WebDriverWait(self.browser, 10).until(lambda driver: driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))
        element.click()


    def get_followers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/followers")
        modal = WebDriverWait(self.browser, 10).until(lambda driver: driver.find_element(By.CLASS_NAME,"_aano"))
        self.followers=set()
        modal.click()
        max=int(self.browser.find_elements(By.CLASS_NAME,"_ac2a")[1].text)
        scroll_start=0
        scroll_end=0
        while len(self.followers)<max:
            self.browser.execute_script("""
            let modal=document.querySelector('._aano')
            console.log({scroll_start})
            modal.scroll({scroll_start},{scroll_end}))""".replace("{scroll_start}",str(scroll_start)).replace("{scroll_end}",str(scroll_end))) 
            scroll_start=scroll_end
            scroll_end += 100
            followers = WebDriverWait(modal, 10).until(lambda driver: driver.find_elements(By.CLASS_NAME, "qi72231t"))

            for user in followers:
                self.followers.add(user.get_attribute("href"))
        print(self.followers)

    def follow_user(self,username):
        pass

    def unfollow_user(self,username):
        pass

    def __del__(self):
        time.sleep(10)
        # self.browser.close()

app=Instagram(os.environ.get("INSTAGRAM_USERNAME"),os.environ.get("INSTAGRAM_PASSWORD"))
app.sign_in()
app.get_followers()