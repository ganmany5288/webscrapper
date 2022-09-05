import requests
import csv
from bs4 import BeautifulSoup


class GraphicsCard:
    type = 'GPU'

    def __init__(self, model, price):
        # Instance Variable
        self.model = model
        self.price = price

#  Get request from a page of GPU

r = requests.get("https://www.memoryexpress.com/Category/VideoCards")
# r = requests.get("https://www.memoryexpress.com/Category/VideoCards?PageSize=120&Page=2")

# Parses request
soup = BeautifulSoup(r.content,'html.parser')

# GPU Price
price = soup.find_all('div', class_ = 'c-shca-icon-item__summary-list')
# print(len(price))
# print(price)

# GPU Title
title = soup.find_all('div', class_ = 'c-shca-icon-item__body-name')
# print(title)

filename = 'gpu_records.csv'
fieldname = ['Title', 'Price']
something = []
rows = []
for i in range(len(price)):
    # print(i)
    t1 = title[i].find('a').text.strip()
    p1 = price[i].find('span').text.strip()
    # b = GraphicsCard(t1,p1)
    # something.append(b)
    if ('RTX' in t1 or 'RX' in t1):
        print(t1)
        test = [t1,p1]
        rows.append(test)

    # print(GraphicsCard(title[i],price[i]))


# print(something)
# print(len(something))
# print(something[0].model)
# print(something[0].price)

# print(rows)
with open(filename,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fieldname)
    csvwriter.writerows(rows)


# csvfile.close()

