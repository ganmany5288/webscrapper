import requests
import csv
from bs4 import BeautifulSoup


class GraphicsCard:

    def __init__(self, brand, model, price):
        # Instance Variable
        self.brand = brand
        self.model = model
        self.price = price

#  Get request from a page of GPU

r = requests.get("https://www.memoryexpress.com/Category/VideoCards")
# r = requests.get("https://www.memoryexpress.com/Category/VideoCards?PageSize=120&Page=2")

# Parses request
soup = BeautifulSoup(r.content,'html.parser')
# print(soup)

# GPU Price
price = soup.find_all('div', class_ = 'c-shca-icon-item__summary-list')
# print(len(price))
# print(price)

# GPU Title, returns a list of objects
title = soup.find_all('div', class_ = 'c-shca-icon-item__body-name')
# print(title)
# Remember that XFX and Zotac uses c-shca-icon-item__body-name-brand and uses .text unlike the rest of the brand.


nvidia_gpu = ["3060", "3060 Ti", "3070", "3070 Ti", "3080", "3080 Ti", "3090", "3090 Ti"]
amd_gpu = ["6700", "6700 XT", "6800", "6800 XT", "6900", "6900 XT"]

brand = title[2].find('img', title = "EVGA")
# print(brand)
# print(brand.title)
# print(brand.text)





filename = 'gpu_records2.csv'
brand = ""
fieldheader = ['Brand','Title', 'Price']
something = []
rows = []

# with open(filename,'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(fieldheader)
#     csvwriter.writerows(rows)


# csvfile.close()




def check_gpu_brand(price,title,brand):
    for i in range(len(price)):
        t1 = title[i].find('a').text.strip()
        p1 = price[i].find('span').text.strip()
        # p1 = price[i].find('span').text.strip()
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
        else:
            print("This is an INVALID CARD")
    print("This is the end")
    filewrite()


def check_gpu_price_title(t1, p1, brand):
    for j in range(len(nvidia_gpu)):
        if nvidia_gpu[j] in t1:
            test = [brand, nvidia_gpu[j], p1]
            rows.append(test)

def filewrite():
    print("I am here")
    print(rows)
    with open(filename,'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fieldheader)
        csvwriter.writerows(rows)

    csvfile.close()


check_gpu_brand(price, title, brand)