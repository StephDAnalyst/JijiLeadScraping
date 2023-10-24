from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json
import time
import csv
import os
options = webdriver.ChromeOptions()
service = Service(executable_path="C:\\Program Files (x86)\\Chromedriver\\chromedriver.exe")
#options.headless = True
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://jiji.ng/computers-and-laptops?filter_attr_176_type=Laptop")
base_url = "https://jiji.ng" 
time.sleep(5)
itemz = []
itemtarcount = 10
previous_height = driver.execute_script("return document.body.scrollHeight")
# itemtarcount = 50
# cont = "//div[@class='b-list-advert-base__data__inner']"
# showcon = "//div[@class='h-flex-center b-btn b-btn--main h-bold h-height-40 h-width-100p']"
while itemtarcount > len(itemz):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  #
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == previous_height:
        break
    previous_height = new_height
    
    textelements = []
    wait = WebDriverWait(driver, 10)
    elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@class, 'b-list-advert-base')]")))

    for element in elements:
        href = element.get_attribute("href")
        full_url = href
        print(full_url)
        jijipg = {'URLS':full_url}
        textelements.append(jijipg)
        
    itemz.extend(textelements)


file_name = 'link_lists.csv'
file_exists = os.path.isfile(file_name)

with open(file_name, 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['URLS'])

    # Write header only if the file is newly created
    if not file_exists:
        writer.writeheader()

    writer.writerows(itemz)     

time.sleep(10)
# Load the saved cookies from the file
with open('cookies.json', 'r') as file:
    cookies = json.load(file)

# Visit the website
driver.get("https://jiji.ng/computers-and-laptops?filter_attr_176_type=Laptop")

# Add the saved cookies to the browser
for cookie in cookies:
    driver.add_cookie(cookie)

# Refresh the page to apply the cookies
driver.refresh()

time.sleep(5)
seller_info_list = []

with open('link_lists.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row if it exists
    for row in reader:
        seller_url = row[0]
        driver.get(seller_url)
        time.sleep(5) 

        showcon = "//div[contains(@class, 'b-button') and contains(text(), 'Show contact')]"

        show_contact_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, showcon))
        )
        driver.execute_script("arguments[0].scrollIntoView();", show_contact_element)
        num = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, showcon))
        )
        num.click()

        try:
            phone_number = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='b-show-contacts-popover-item__phone h-flex-1-0 h-mr-15']"))
            )
        except TimeoutException:
            phone_number = "Phone number not available"
        SellerName = driver.find_element(By.XPATH, "//div[@class='b-seller-block__name']")
        laptopName = driver.find_element(By.XPATH, "//h1[@itemprop='name']")
        Cost = driver.find_element(By.XPATH, "//span[@class='qa-advert-price-view-title b-alt-advert-price__text']")

        jijipg = {
                        'SellName': SellerName.text,
                        'Laptop': laptopName.text,
                        'Price': Cost.text,
                        'phone': phone_number.text
                    }
        print(jijipg)
        seller_info_list.append(jijipg)
        
print(len(seller_info_list))

file_name = 'seller_info.csv'

with open(file_name, 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['SellName', 'Laptop', 'Price', 'phone']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(seller_info_list)

# Quit the browser
driver.quit()       
                

