import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

config = load_dotenv("D:\\Udemy1\\Python\\.env")
driver = webdriver.Chrome(os.getenv("chrome_driver_path"))

try:
	driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
	# search = driver.find_element(By.NAME, "search")
	# search.send_keys("Python")
	# search.send_keys(Keys.ENTER)
	login = driver.find_element(By.CSS_SELECTOR, "#pt-createaccount-2 a")
	login.click()

except:
	driver.close()
finally:
	driver.close()
