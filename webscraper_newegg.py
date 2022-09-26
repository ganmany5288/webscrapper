import requests
import csv
from bs4 import BeautifulSoup
from time import sleep

# class GraphicsCard:

#     def __init__(self, brand, model, price):
#         # Instance Variable
#         self.brand = brand
#         self.model = model
#         self.price = price

# pages = [
#     "https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7708&PageSize=96"
# ]

# Remember that XFX and Zotac uses c-shca-icon-item__body-name-brand and uses .text unlike the rest of the brand.


gpu_name = ["3060", "3060 Ti", "3070", "3070 Ti", "3080", "3080 Ti", "3090", "3090 Ti","6700", "6700 XT", "6800", "6800 XT", "6900 XT", "6950 XT"]
new_gen_gpu = ["4060","4060 Ti","4070","4070 Ti","4080", "4080 Ti","4090", "4090 Ti"]

filename = 'gpu_recordsFORREAL_newegg2.csv'
brand = ""
fieldheader = ['Brand','Title', 'Price']
something = []
rows = []

def check_gpu_brand(price,title,brand):
    for i in range(len(price)):
        t1 = title[i].text
        p1 = price[i].text
        print(t1, p1)
        """
            Check the following GPU Brands
            1. MSI
            2. EVGA
            3. Gigabyte
            4. Asus
        """

        if ("EVGA" in t1):
            brand = "EVGA"
            check_gpu_price_title(t1, p1, brand)
        elif ("MSI" in t1):
            # print("This is an MSI Graphics card")
            brand = "MSI"
            check_gpu_price_title(t1, p1,brand)
        elif ("GIGABYTE" in t1):
            # print("This is a Gigabyte Graphics card")
            brand = "Gigabyte"
            check_gpu_price_title(t1, p1, brand)
        elif ("ASUS" in t1):
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
        # csvwriter.writerow(fieldheader)
        csvwriter.writerows(rows)

    csvfile.close()


pages = [
    "https://www.newegg.ca/Desktop-Graphics-Cards/SubCategory/ID-48?Tid=7708&PageSize=96",
]


with open(filename, 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fieldheader)

csvfile.close()
for page in pages:
    r = requests.get(page)
    soup = BeautifulSoup(r.content,'html.parser')
    price = soup.find_all('li', class_ = 'price-current')
    title = soup.find_all('a', class_ = 'item-title')
    brand = ""
    # print(price, title)
    print("I am here")
    check_gpu_brand(price, title, brand)
    print("Am here now")
    sleep(10)