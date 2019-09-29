from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.flipkart.com').text
soup = BeautifulSoup(source, 'lxml')

itemName = []
itemDicount = []

for nameofitem in soup.find_all('div', class_='iUmrbN'):
    textnameofitem = nameofitem.text
    itemName.append(textnameofitem)
for discount in soup.find_all('div', class_='BXlZdc'):
    textdiscount = discount.text
    itemDicount.append(textdiscount)

for i in range(len(itemName)):
    print(itemName[i])
    print(itemDicount[i])
    print()