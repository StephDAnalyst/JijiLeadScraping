# Jiji Web Crawler
This documentation provides a concise overview of a Python web scraping project that uses Selenium and Chrome WebDriver to extract data from the Jiji website. The project comprises three primary sections: logging in, scraping laptop listings/URLs, saving data to CSV files, and loading and scraping data from saved URLs.

Overview
The Jiji Web crawler streamlines the process of automatically extracting laptop listings and seller contact information from the Jiji website. It leverages Selenium, a well-known web automation framework, in conjunction with Chrome WebDriver to interact with the website.

## Execution Guidelines
To execute the code, follow these clear-cut instructions:

**ChromeDriver Installation:** Ensure that you have ChromeDriver installed, with version 84 recommended for this project. It is essential to maintain version compatibility between ChromeDriver and your Chrome browser for seamless operations.

**Virtual Environment (Recommended):** We strongly recommend setting up a virtual environment for this project. This not only simplifies dependency management but also provides a controlled and isolated environment for web scraping tasks.

**Selenium Installation:** Confirm that Selenium is correctly installed within your virtual environment.

## Logging In
This section automates the login process to the Jiji website and encompasses the following steps:

1. Navigate to the Jiji laptop website.
2. Perform a secure login using your personal credentials.
3. Save your session cookies to a JSON file for future use.
   
## Scraping Laptop Listings on Jiji

This segment of the project focused on extracting laptop listings from the Jiji website. The primary steps are as follows:

1. Scroll through the webpage to load additional listings.
2. Extract URLs for individual laptop listings.
3. Save these URLs for later retrieval.
4. Load the saved URLs and apply saved cookies to access the necessary data.

## Conclusion
This project helps users with the ability to crawl the Jiji website, extract important data, including phone numbers, and serve as a valuable resource for lead generation.

Feel free to explore the project's code repository and make any necessary enhancements or customizations to align it with your specific requirements.
