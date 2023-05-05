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


display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)

    
driver = webdriver.Chrome(options = chrome_options)

url = 'https://tienda.umbro.com.ar/botines/42?initialMap=c&initialQuery=botines&map=category-1,talle&order=OrderByPriceDESC'
driver.get(url)
is_available = False
output = ""

# Esperar a que la página cargue completamente
titles = WebDriverWait(driver, 10).until(lambda x: x.find_elements(By.CLASS_NAME, "vtex-product-summary-2-x-productBrand"))
prices = WebDriverWait(driver, 10).until(lambda x: x.find_elements(By.CLASS_NAME, "glamit-product-price-0-x-sellingPriceValue"))

# Iterar sobre los elementos y obtener el innerHTML
for title in titles:
    title_text = title.text
    for price in prices:
        price_text = price.text
        if title_text == "BOTIN SALA UMBRO PRO 5 BUMP" or title_text == "BOTIN SINTETICO UMBRO SPECIALI III PRO":
        # BOTIN SINTETICO UMBRO PRO 5 BUMP CLUB
            output += "<h3>" + title_text + "</h3>"
            output += "<p>" + price_text + "</p>"
            output += "<br/>"
            is_available = True
    continue


output += f"<a href='{url}'>Ir a la tienda</a>"


# ------------------------------------------------------

# Configuración del servidor SMTP y de las credenciales
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'dentalturno@gmail.com'
SMTP_PASSWORD = 'xcgyjoaatrrvyvhm'


# Configuración del mensaje
msg = MIMEMultipart()
msg['From'] = '"Umbro Botines" <dentalturno@gmail.com>'
msg['To'] = 'tobsailbot@gmail.com'
msg['Subject'] = 'BOTINES DISPONIBLES - Umbro Web Scraping Selenium'


if is_available:
    # Agregar el cuerpo del mensaje
    msg.attach(MIMEText(output, "html"))

    # Enviar el correo electrónico
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
