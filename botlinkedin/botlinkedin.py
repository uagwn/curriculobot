from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

username="wagnyoliver@gmail.com"
password = "Deasilva134!"



driver = webdriver.Firefox()

driver.get("https://www.linkedin.com/login")

driver.implicitly_wait(5)

time.sleep(5)

user = driver.find_element(By.XPATH, '//*[@id="username"]')
user.send_keys(username) 

user = driver.find_element(By.XPATH, '//*[@id="password"]')
user.send_keys(password) 

time.sleep(5)

login = driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]')
login.click()


time.sleep(25)

driver.implicitly_wait(10)

driver.get("https://www.linkedin.com/jobs/")

body = driver.find_element(By.TAG_NAME, 'body')
for _ in range(10): 
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)  
        
elementos_links = driver.find_elements(By.XPATH, '//a[contains(@href, "/jobs/view/")]')

urls = [elemento.get_attribute('href') for elemento in elementos_links]

urls = [url for url in urls if url]  # Remove URLs None
for url in urls:
    print(url)