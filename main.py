from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = "UPDATE THE USERNAME VARIABLE"
password = "UPDATE THE PASSWORD VARIABLE"
description = "UPDATE THE DESCRIPTION VARIABLE"

driver = webdriver.Chrome()
driver.get("https://www.roblox.com/login")

# logging in into the account
driver.find_element(By.ID, "login-username").send_keys(username)
driver.find_element(By.ID, "login-password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

time.sleep(3)

# navigates to the profile
driver.find_element(By.CLASS_NAME, "avatar").click()

time.sleep(3)

# storing old description into the variable, then writing a new description and saving it
oldDecsription = driver.find_element(By.ID, "profile-about-text").text
driver.find_element(By.CLASS_NAME, "btn-generic-edit-sm").click()
driver.find_element(By.ID, "descriptionTextBox").clear()
driver.find_element(By.ID, "descriptionTextBox").send_keys(description)
driver.find_element(By.ID, "SaveInfoSettings").click()

time.sleep(3)

# output
textbox = driver.find_element(By.ID, "profile-about-text").text
if description in textbox:
    print(F"Old description: {oldDecsription}.")
    print(f"New description: {textbox}.")
    print("\nTest passed. Description was changed.")
else:
    print(f"Current description: {textbox}.")
    print("Test failed.")

driver.quit()
