# Hi, Shopify!

This is my take on the Shopicruit challenge. I've been meaning to get some experience with Python (and pandas),
so I took this as a chance to get started. Running `product_counter.py` should give the total cost of every wallet
and lamp (985.52).

## Watch this space!
The current script should meet the specifications, but I'm not a bare-minimum kind of guy. I want to keep working
with pandas to try and extract some interesting insights/statistics from the data. End goal would be to get some
nice visualizations of the data too.

(Current challenge: the structure of the data in Python is a little perculiar; notably the one-to-many mapping from
products to variants in a single row. Intuitively, it seems that working with this data would be easier if it were
"flat;" i.e. one entry for each _variant_, not product. We could group by product when desired to get the broader
picture).

## Potential problems (and solutions)
### Fragile search
Right now, I'm using the basic Python `in` operator to check if the product type matches `Wallet` or `Lamp`. This 
solution will fail if the product type is given as, for example, `lamp` (case matters). I validated that this 
assumption (i.e. the only product types we want are `Wallet`/`Lamp`) was accurate (for this dataset) via a mix of 
`grep` and manual inspection of several product entries. Given any sort of "real-world" data, we would want to 
utilise much more advanced methods for this matching.
(Regular expressions would be a good start, but I would be wary of potential performance impacts. Might be feasible
for optimsed patterns; would require some performance testing to validate).

### Hardcoded "allowed" product types and file
Obviously in a real-world scenario, we would like to generalize our script to take some parameters and perform some
more sophisticated actions.

### Product availability
The current solution also totally ignores whether the items we want are actually available, what currency the price 
is in, and if there's shipping costs we need to factor in. Important factors to consider! Thankfully, that 
information (and more) is in the data, and we could include that in our search fairly easily.
