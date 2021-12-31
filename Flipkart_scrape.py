
import requests
import json
from bs4 import BeautifulSoup


product = input('Enter product Name : ')
filename = input('File name to Store Output : ')

url = f"https://www.flipkart.com/search?q={product}"

a = 0
while a < 10000:
    print('.', end='')
    data = requests.get(url).content
    a = len(data)
    print(a)
print()


soup = BeautifulSoup(data, 'html.parser')


def vertical(blocks):
    for index, block in enumerate(blocks):
        img = block.find('img', {"class": "_396cs4"})['src']
        name = block.find('div', {"class": "_4rR01T"}).string
        rating = block.find('span', {"class": "_1lRcqv"}).find('div').text
        features = block.find('ul', {"class": "_1xgFaf"}).contents
        specs = ''
        for feature in features:
            specs += f"{feature.text}\n"

        print(f"Sno:{index}")
        print(f"name= {name}\nrating= {rating}\nimg= {img}")
        print(specs)

# def horizontal(blocks):
#     for index,block in enumerate(blocks):
#         img = block.find('img', {"class": "_396cs4"})['src']
#         name = block.find('div', {"class": "_4rR01T"}).string
#         rating = block.find('span', {"class": "_1lRcqv"}).find('div').text


blocks = soup.findAll('a', {"class": "_1fQZEK"})
if len(blocks) != 0:
    vertical(blocks)
else:

    blocks = soup.findAll('div', {"class": "_13oc-S"})
    print(len(blocks))
    Product_list = []
    for index, block in enumerate(blocks):
        new_product = {}
        new_product['id'] = index
        new_product['img'] = block.find('img', {'class': '_396cs4'})['src']
        new_product['name'] = block.find('a', {"class": "s1Q9rs"}).string
        new_product['rating'] = block.find('div', {"class": "_3LWZlK"}).text
        new_product['price'] = block.find('div', {'class': '_30jeq3'}).text
        Product_list.append(new_product)

    with open(f'./Flipkart_{filename}', 'w') as file:
        file.write(json.dumps(Product_list))
