#!/usr/bin/python

import json
import pandas as pd
import numpy as np

allowed_types = ["Wallet", "Lamp"]

with open('products.json') as data_file:    
    data = json.load(data_file)

df = pd.DataFrame(data['products'])

wanted_products = df[df.product_type.isin(allowed_types)]

total_cost = 0.0

for product in wanted_products.variants:
    for variant in product:
        total_cost += float(variant['price'])

print(total_cost)
