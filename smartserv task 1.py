import requests
import json
import pandas as pd

r = requests.get('https://s3.amazonaws.com/open-to-cors/assignment.json')
json_Data = json.loads(r.text)

price = []
for itemprice in json_Data:
    price.append(json_Data)

df = pd.DataFrame(data=price, columns=['subcategory', 'title', 'price', 'popularity'])
print(df.head())

