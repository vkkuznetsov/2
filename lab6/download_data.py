import requests
from bs4 import BeautifulSoup

# Получите HTML-код страницы
url = 'http://socr.ucla.edu/docs/resources/SOCR_Data/SOCR_Data_Dinov_020108_HeightsWeights.html'
response = requests.get(url)
html = response.text

# Разбор HTML с помощью BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Извлеките данные из таблицы
table = soup.find('table')
data = []
for row in table.find_all('tr'):
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells]
    data.append(row_data)

# Обработайте и сохраните данные
# Например, вы можете сохранить их в CSV-файл
import csv
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row)