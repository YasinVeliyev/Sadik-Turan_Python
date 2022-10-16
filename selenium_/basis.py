import time

from selenium import webdriver

chrome_driver_path = "D:\\Udemy1\\Python\\chromedriver.exe"
url = "https://github.com/"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
time.sleep(1)
driver.maximize_window()
driver.get(url + "YasinVeliyev")
driver.save_screenshot("github.png")

time.sleep(1)
print(driver.title)
driver.close()
