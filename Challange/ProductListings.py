import json
from pprint import pprint

data =
with open('products.txt', 'rt') as data_file:


    for line in data_file:
        data.append(json.loads(line))


with open('listings.txt', 'rt') as data_file:


    for line in data_file:
        json.loads(line)
