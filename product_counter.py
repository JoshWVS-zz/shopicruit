#!/usr/bin/python

import json
import pandas as pd
import numpy as np

allowed_types = ["Wallet", "Lamp"]

with open('products.json') as data_file:    
    data = json.load(data_file)

df = pd.DataFrame(data['products'])

test = df[df.product_type.isin(allowed_types)]
print(test)
