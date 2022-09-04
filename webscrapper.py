# from bs4 import BeautifulSoup
# soup = 


# import requests
# page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
# print(page.content)


# import requests
# from bs4 import BeautifulSoup

# page = requests.get("https://www.amazon.ca/gp/product/B08Z4J6NHW/ref=ox_sc_act_title_1?smid=A3DWYIK6Y9EEQB&psc=1")
# print(page.content)


# soup = BeautifulSoup(page.content,'html.parser')
# print(soup.prettify())


# import requests
# from bs4 import BeautifulSoup

# r = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

# # print(r.content)
# soup = BeautifulSoup(r.content,'html.parser')
# # print(soup)

# s = soup.find('div', class_='entry-content')
# # print(s)

# content = s.find_all('p')

# print(content)



import requests
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

# Prints out the title of every GPU in memx within page 1
# for t in title:
#     print(t.find('a').text.strip())

# Prints out the price of every GPU in memx within page 1
# for p in price:
#     print(p.find('span').text.strip())

something = []

for i in range(len(price)):
    # print(i)
    t1 = title[i].find('a').text.strip()
    p1 = price[i].find('span').text.strip()
    b = GraphicsCard(t1,p1)
    something.append(b)
    # print(GraphicsCard(title[i],price[i]))

# print(something)
# print(len(something))
print(something[0].model)
print(something[0].price)



