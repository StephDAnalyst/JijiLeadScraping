from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Navigate to the Jiji laptop website
driver.get("https://jiji.ng/computers-and-laptops?filter_attr_176_type=Laptop")

# Locate the "Sign In" link using the given XPath
sign_in_link = driver.find_element(By.XPATH, "//a[@href='/login.html' and @class='h-flex-center']")

# Click on the "Sign In" link
sign_in_link.click()

# Wait for the presence of the email or phone input field
wait = WebDriverWait(driver, 30)
email_phone_input = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'E-mail or phone')]")))

# Click on the "E-mail or phone" input field
email_phone_input.click()

# Input the email or phone number
emailinput = wait.until(EC.presence_of_element_located((By.XPATH, "//input[contains(@class, 'qa-login-field')]")))
emailinput.send_keys("stephniechikaodili@gmail.com")

# Locate the password input field and input the password
password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
password_input.send_keys("0813636Li")

# Locate and click the "Log in" button
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'SIGN IN')]")))
login_button.click()
time.sleep(5)
# Save the cookies to a file
cookies = driver.get_cookies()
with open('cookies.json', 'w') as file:
    json.dump(cookies, file)

driver.quit()
