# Jiji Web Crawler

This documentation provides an overview of a Python web scraping and Crawling project using Selenium and Chrome WebDriver to extract data from the Jiji website. The project is divided into three main sections: logging in, scraping laptop listings/urls, saving data to CSV files, and loading and scraping data from saved URLs.

## Overview

The Jiji Web Scraper is designed to automate the process of extracting laptop listings and seller contact information from the Jiji website. It uses Selenium, a popular web automation framework, and Chrome WebDriver to interact with the website.

## Logging In

In this section, the script automates the process of logging in to the Jiji website. It includes the following steps:

1. Navigating to the Jiji laptop website.
2. Loggiing in with your personal details
3. Saving your cookies to a json file
4. Scraping urls of laptop sellers from Jiji
5. Visting the site again to apply the saved cookies
6. Loading and Scraping Data from Saved URLs

### Code Example

```python
# Import necessary libraries
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

# Configure Chrome WebDriver with options and service
options = webdriver.ChromeOptions()
service = Service(executable_path="C:\\Program Files (x86)\\Chromedriver\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# ... (other code for logging in)
```

## Scraping Laptop Listings on Jiji
This section of the project focuses on scraping laptop listings from the Jiji website. The key steps include:

1. Scrolling through the page to load more listings.
2. Extracting URLs for individual laptop listings.
3. Saving these URLs for later use.
4. Load the saved urls and applying saved cookies to obtain the needed data
Code Example
```python
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
#... other code for data extraction and lead scraping on jiji
```

## Conclusion
This project demonstrates how to use Python and Selenium for web scraping. It allows users to crawl the Jiji website and extract the phone numbers as well as other important information from the website.

Feel free to explore the code in the repository and make improvements or modifications to suit your requirements.
