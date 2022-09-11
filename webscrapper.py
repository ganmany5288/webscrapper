import requests
import csv
from bs4 import BeautifulSoup
from time import sleep


class GraphicsCard:

    def __init__(self, brand, model, price):
        # Instance Variable
        self.brand = brand
        self.model = model
        self.price = price

pages = [
    "https://www.memoryexpress.com/Category/VideoCards?PageSize=120",
    "https://www.memoryexpress.com/Category/VideoCards?PageSize=120&Page=2"
]



#  Get request from a page of GPU
r = requests.get("https://www.memoryexpress.com/Category/VideoCards")

# Parses request
soup = BeautifulSoup(r.content,'html.parser')

# GPU Price
price = soup.find_all('div', class_ = 'c-shca-icon-item__summary-list')

# GPU Title, returns a list of objects
title = soup.find_all('div', class_ = 'c-shca-icon-item__body-name')
# Remember that XFX and Zotac uses c-shca-icon-item__body-name-brand and uses .text unlike the rest of the brand.


gpu_name = ["3060", "3060 Ti", "3070", "3070 Ti", "3080", "3080 Ti", "3090", "3090 Ti","6700", "6700 XT", "6800", "6800 XT", "6900 XT", "6950 XT"]

filename = 'gpu_recordsFORREAL2.csv'
brand = ""
fieldheader = ['Brand','Title', 'Price']
something = []
rows = []

def check_gpu_brand(price,title,brand):
    for i in range(len(price)):
        t1 = title[i].find('a').text.strip()
        p1 = price[i].find('span').text.strip()
        """
            Check the following GPU Brands
            1. MSI
            2. EVGA
            3. Gigabyte
            4. Asus
            5. XFX and Zotac brands will be included later
        """

        if (title[i].find('img', title = "EVGA")):
            brand = "EVGA"
            check_gpu_price_title(t1, p1, brand)
        elif (title[i].find('img', title = "MSI")):
            # print("This is an MSI Graphics card")
            brand = "MSI"
            check_gpu_price_title(t1, p1,brand)
        elif (title[i].find('img',title = "Gigabyte")):
            # print("This is a Gigabyte Graphics card")
            brand = "Gigabyte"
            check_gpu_price_title(t1, p1, brand)
        elif (title[i].find('img', title = "Asus")):
            # print("This is an Asus Graphics card")
            brand = "Asus"
            check_gpu_price_title(t1, p1, brand)
    filewrite()


def check_gpu_price_title(t1, p1, brand):
    for j in range(len(gpu_name)):
        if gpu_name[j] in t1:
            test = [brand, gpu_name[j], p1]
            rows.append(test)

def filewrite():
    # print("I am here")
    # print(rows)
    with open(filename,'a') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fieldheader)
        csvwriter.writerows(rows)

    csvfile.close()


pages = [
    "https://www.memoryexpress.com/Category/VideoCards?PageSize=120",
    "https://www.memoryexpress.com/Category/VideoCards?PageSize=120&Page=2"
]



#  Get request from a page of GPU
r = requests.get("https://www.memoryexpress.com/Category/VideoCards")

# Parses request
soup = BeautifulSoup(r.content,'html.parser')

# GPU Price
price = soup.find_all('div', class_ = 'c-shca-icon-item__summary-list')

# GPU Title, returns a list of objects
title = soup.find_all('div', class_ = 'c-shca-icon-item__body-name')

for page in pages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content,'html.parser')
    price = soup.find_all('div', class_ = 'c-shca-icon-item__summary-list')
    title = soup.find_all('div', class_ = 'c-shca-icon-item__body-name')
    brand = ""
    check_gpu_brand(price, title, brand)
    sleep(10)