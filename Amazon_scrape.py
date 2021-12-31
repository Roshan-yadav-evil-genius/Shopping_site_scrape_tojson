import requests
from bs4 import BeautifulSoup
import json

product = input('Enter product Name : ')
filename = input('File name to Store Output : ')

url = f'https://www.amazon.in/s?k={product}'

a = 0
while a < 10000:
    print('.', end='')
    data = requests.get(url).content
    a = len(data)
    print(a)
print()

soup = BeautifulSoup(data, 'html.parser')

a = soup.findAll('div', {"data-component-type": "s-search-result"})
Product_list = []
for index, content in enumerate(a):
    new_product = {}
    new_product['id'] = index
    new_product['img'] = content.find('img')['src']
    new_product['name'] = content.find('h2').span.string
    new_product['rating'] = content.find(
        'span', {'class': 'a-icon-alt'}).string
    new_product['price'] = content.find(
        'span', {'class': 'a-price-whole'}).string
    Product_list.append(new_product)


with open(f'./Amazon_{filename}', 'w') as file:
    file.write(json.dumps(Product_list))
