from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json
import chromedriver_autoinstaller
from pprint import pprint


# chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
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

url = 'https://www.expatistan.com/es/costo-de-vida/pais/argentina'
driver.get(url)

# Esperar a que la página cargue completamente
table = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.XPATH, '''//*[@id="content"]/div/div[3]/table'''))

# Encuentra todas las filas de la tabla
rows = table.find_elements(By.TAG_NAME, 'tr')

# Lista de datos
json_list = {}
big_data = []

data = {}
data_array = []

# Itera a través de las filas e imprime el contenido de las celdas
for row in rows:
    all_rows = row.find_elements(By.TAG_NAME, 'th') + row.find_elements(By.TAG_NAME, 'td')

    for cell in all_rows:
        if cell.text != '':
            if "th" in cell.tag_name:
                header = cell.text
                data_array = []
                json_list = {}
                big_data.append(json_list)

            if "name" in cell.get_attribute('class'):
                data['name'] = cell.text

            if "price" in cell.get_attribute('class'):
                data['price'] = cell.text

    if data:
        data_array.append(data)
        json_list['header'] = header
        data = {}
        json_list['data'] = data_array

pprint(big_data)

# Cierra el navegador cuando hayas terminado
driver.quit()


# Guarda los datos en un archivo JSON
with open('datos.json', 'w', encoding='utf-8') as json_file:
    json.dump(big_data, json_file, ensure_ascii=False, indent=4)
