from selenium import webdriver

chrome_driver_path = "D:\\Udemy1\\Python\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.sadikturan.com/")
print(dir(driver))
