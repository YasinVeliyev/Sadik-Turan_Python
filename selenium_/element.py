from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\\Udemy1\\Python\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
try:

	driver.get(
		"https://www.n11.com/urun/next-ye-32020kt-32-hd-dahili-uydu-alicili-led-tv-1345332?magaza=ziboxelektronik")

	title = driver.find_element(By.CLASS_NAME, "proName")
	price = driver.find_element(By.CLASS_NAME, "newPrice").find_element(By.TAG_NAME, "ins")
	search = driver.find_element(By.ID, "searchData").get_attribute("value")
	
	print(title.text, price.text, search, sep="\n")
except:
	driver.close()
finally:
	driver.close()
