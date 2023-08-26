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
data_cells = []

# Itera a través de las filas e imprime el contenido de las celdas
index = -1
cell_index = 0

# for row in rows:
#     header_cells = row.find_elements(By.TAG_NAME, 'th')
#     cells = row.find_elements(By.TAG_NAME, 'td')
#     all_rows = header_cells + cells

#     if header_cells:
#         for header in header_cells:
#             if header.text:
#                 header_data =[ {
#                     "header": header.text
#                 }]
#                 data_list.append(header_data)
#                 index += 1


#     for cell in cells:
#         if cell.text:
#             cell_data = {}
#             if "name" in cell.get_attribute('class'):
#                 cell_data['name'] = cell.text

#             if "price" in cell.get_attribute('class'):
#                 cell_data['price'] = cell.text
#             if cell_index == 1:
#                 print(cell_data)
#                 data_cells.append(cell_data)
#                 cell_index = 0
#             # cell_data.append(data)
#             # data_list[index]['data'] = cell_data
#             # print(cell.get_attribute('class'))
#             cell_index += 1
    
#     print(index)

data = {}
data_array = []

for row in rows:

    all_rows = row.find_elements(By.TAG_NAME, 'th') + row.find_elements(By.TAG_NAME, 'td')

    header = ''
    for cell in all_rows:
        if cell.text:
            if "th" in cell.tag_name:
                index += 1
                print(index)
                header = cell.text

            if "price" in cell.get_attribute('class'):
                data['price'] = cell.text

            if "name" in cell.get_attribute('class'):
                data['name'] = cell.text
    print('--------------')
    # pprint(data)
    print(header)
    if data and index == 0:
        json_list['header'] = header
        data_array.append(data)
    data = {}
    
    json_list['data'] = data_array


# pprint(data_array)
pprint(json_list)
# pprint(data_cells)

# Cierra el navegador cuando hayas terminado
driver.quit()
