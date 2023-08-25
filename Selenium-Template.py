from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import chromedriver_autoinstaller
from pyvirtualdisplay import Display


# display = Display(visible=0, size=(800, 800))  
# display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors",
 
    "--headless",
    "--disable-gpu",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage",
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

url = 'https://tienda.umbro.com.ar/botines/42?initialMap=c&initialQuery=botines&map=category-1,talle&order=OrderByPriceDESC'
driver.get(url)

# Esperar a que la página cargue completamente
titles = WebDriverWait(driver, 10).until(lambda x: x.find_elements(By.CLASS_NAME, "vtex-product-summary-2-x-productBrand"))
prices = WebDriverWait(driver, 10).until(lambda x: x.find_elements(By.CLASS_NAME, "glamit-product-price-0-x-sellingPriceValue"))

