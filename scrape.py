from bs4 import BeautifulSoup
import requests

source = requests.get('https://old.uinp.gov.ua/publication/derzhavnii-gimn-ukraini').text

soup = BeautifulSoup(source, 'lxml')

# Title and paragraphs
title = soup.find('h1', class_='pagetitle').text
print(title)

for paragraph in soup.find_all('p', class_="rtecenter"):
    print(paragraph.text)

# In HTML format body
for part in soup.find_all('p', class_="rtecenter"):
    print(part.prettify())
