#!/usr/bin/python

import json
import pandas as pd
import numpy as np

with open('products.json') as data_file:    
    data = json.load(data_file)

df = pd.DataFrame(data['products'])

print(df.head())
