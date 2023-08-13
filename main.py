from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

chrome_path = os.environ.get("CHROMIUM_PATH")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(executable_path=f"r{chrome_path}"), options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/")

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()
time.sleep(3)
username_input = driver.find_element(By.ID, "username")
username_input.send_keys(os.environ.get("LKD_USR"))
password_input = driver.find_element(By.ID, "password")
time.sleep(1)
password_input.send_keys(os.environ.get("LKD_PWD"))
password_input.send_keys(Keys.ENTER)

time.sleep(15)

job_links = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results-list li a")

for link in job_links:
    link.click()
    time.sleep(1)
    jobs_save_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    try:
        jobs_save_btn.click()
    except:
        pass