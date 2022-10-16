import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

config = load_dotenv("D:\\Udemy1\\Python\\.env")
blogs = {}
try:
	driver = webdriver.Chrome(os.getenv("chrome_driver_path"))
	driver.minimize_window()
	driver.get("https://www.python.org")
	blog_times = driver.find_elements(By.CSS_SELECTOR, ".blog-widget time")
	blog_names = driver.find_elements(By.CSS_SELECTOR, ".blog-widget li a")
	for i in range(len(blog_times)):
		blogs[i] = {"time": blog_times[i].text, "name": blog_names[i].text}
	# for time in blog_times:
	# 	print(time.text)
	# for name in blog_names:
	# 	print(name.text)
	print(blogs)
except:
	driver.close()
finally:
	driver.close()
