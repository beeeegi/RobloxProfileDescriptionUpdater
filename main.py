from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# logs
logging.basicConfig(filename='logs.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# acc info
username = "username"
password = "password"
description = "hiddendevs ontop??"

# chrome setup
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    # login proccess
    driver.get("https://www.roblox.com/login")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login-username"))).send_keys(username)
    print("Inputted username")
    driver.find_element(By.ID, "login-password").send_keys(password)
    print("Inputted password")
    driver.find_element(By.ID, "login-button").click()
    print("Clicked login button")

    # waiting for the verification button to appear and clicking it
    try:
        verify_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "rostile-verify-button"))
        )
        verify_button.click()
        print("Clicked verify button")
    except Exception as e:
        logging.error(f"Verification button error: {e}")

    # wait for the profile load
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "avatar"))).click()
    print("Profile has been loaded")

    # fetching old description
    old_description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-about-text"))).text
    print("Saved old description: " + old_description)

    # updating description
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-generic-edit-sm"))).click()
    description_textbox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "descriptionTextBox")))
    description_textbox.clear()
    description_textbox.send_keys(description)
    print("Updated description to: " + description)

    # saving new description
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "SaveInfoSettings"))).click()
    print("Description saved")

    # confirming that everything worked
    new_description = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profile-about-text"))).text
    print("New description: " + new_description)

    # output
    if description in new_description:
        logging.info(f"Old description: {old_description}")
        logging.info(f"New description: {new_description}")
        driver.save_screenshot('success_screenshot.png')
        print("Screenshot taken, log file updated")
    else:
        logging.error("Description update failed.")
        driver.save_screenshot('fail_screenshot.png')

except Exception as e:
    logging.error(f"An error occurred: {e}")
    driver.save_screenshot('error_screenshot.png')

finally:
    driver.quit()
