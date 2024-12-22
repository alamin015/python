import pandas as pd


data = pd.read_json('./data/data.json')
new_data =  data.dropna()

print(new_data.to_string())