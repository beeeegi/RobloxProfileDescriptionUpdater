from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = "UPDATE THE USERNAME VARIABLE"
password = "UPDATE THE PASSWORD VARIABLE"
description = "UPDATE THE DESCRIPTION VARIABLE"

driver = webdriver.Chrome()
driver.get("https://www.roblox.com/login")

# logging into the account
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username"))).send_keys(username)
driver.find_element(By.ID, "login-password").send_keys(password)
driver.find_element(By.ID, "login-button").click()

# wait until the profile avatar is clickable and then click it
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "avatar"))).click()

# wait until the profile description is present
old_description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-about-text"))).text

# click the edit button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-generic-edit-sm"))).click()

# clear and enter the new description
description_textbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "descriptionTextBox")))
description_textbox.clear()
description_textbox.send_keys(description)

# click the save button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "SaveInfoSettings"))).click()

# wait until the new description is updated
new_description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-about-text"))).text

# output
if description in new_description:
    print(f"Old description: {old_description}.")
    print(f"New description: {new_description}.")
    print("\nTest passed. Description was changed.")
else:
    print(f"Current description: {new_description}.")
    print("Test failed.")

driver.quit()
