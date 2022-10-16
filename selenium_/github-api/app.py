import os
import time

from dotenv import load_dotenv, find_dotenv, dotenv_values
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv(".env")


class GitHub:
    # profile = webdriver.FirefoxProfile("/home/yasin/snap/firefox/common/.mozilla/firefox/ysik6n0m.yasin")
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    def __init__(self, username, password):
        self.baseUrl = "https://github.com/"
        self.username = username
        self.password = password
        self.followers = []

    def login(self):
        self.browser.get(f"{self.baseUrl}login")
        self.browser.find_element(By.NAME, "login").send_keys(self.username)
        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        self.browser.find_element(By.NAME, "commit").click()

    def find_repositories(self, keyword):
        self.browser.get(self.baseUrl)
        search = self.browser.find_element(By.NAME, "q")
        search.send_keys(keyword)
        search.send_keys(Keys.ENTER)
        time.sleep(1)
        repos = self.browser.find_elements(By.CLASS_NAME, 'repo-list-item')
        self.repos = {}

        for repo in repos:
            anchor = repo.find_element(By.TAG_NAME, "a")
            self.repos[anchor.text] = {"repo_link": anchor.get_attribute("href"),
                                       "description": repo.find_element(By.TAG_NAME, 'p').text}

        print(self.repos)

    def save_followers(self):
        items = self.browser.find_elements(By.CSS_SELECTOR, ".d-table.table-fixed")
        for item in items:
            user_name = item.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "span")[1].text
            name = item.find_elements(By.TAG_NAME, "div")[1].find_elements(By.TAG_NAME, "span")[0].text
            self.followers.append({"username": user_name, "name": name})
        return True

    def get_followers(self, username):
        page = 75
        while True:
            self.browser.get(f"{self.baseUrl}{username}?page={page}&tab=followers")
            self.save_followers()
            page += 1
            anchor = self.browser.find_element(By.CSS_SELECTOR, ".pagination").find_elements(By.TAG_NAME, "a")
            if len(anchor) == 1 and anchor[0].text != "Next":
                break
        print(len(self.followers))

    def __del__(self):
        time.sleep(10)
        print("AAAAAAAAAAAAAAAAAA")
        self.browser.close()


username = os.environ.get("USER_NAME")
password = os.environ.get("PASSWORD")
app = GitHub(username, password)
# app.find_repositories("Python")
app.get_followers("sadikturan")
