#!/usr/bin/python

import json

with open('products.json') as data_file:    
    data = json.load(data_file)

total_cost = 0.0

for unit in data['products']:
    if unit['product_type'] in ["Wallet", "Lamp"]:
        for item in unit['variants']:
            print(unit['product_type'])
            total_cost += float(item['price'])

print(total_cost)
