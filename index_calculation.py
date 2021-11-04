import requests 
import apikey
import json
import pandas as pd
import numpy as np
from datetime import date

# Importing the base data to calculate index

base_data = pd.read_csv('base_data.csv', sep=";", index_col=0)

# Getting fresh data for the fresh index level from the coinmarketcap API

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'100',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': apikey.key
}

json = requests.get(url,params = parameters, headers = headers).json()
coins = json['data']

crypto_data = pd.DataFrame(columns=['id', 'name', 'ticker', 'price', 'supply', 'platform'])

for x in coins:
    
    id_num = x['id']
    name = x['name']
    symbol = x['symbol']
    price = x['quote']['USD']['price']
    supply = x['total_supply']
    platform = x['platform']
    
    crypto_data = crypto_data.append({'id':id_num, 'name':name, 'ticker':symbol, 'price':price, 'supply':supply,
                                      'platform':platform}, ignore_index=True)


# Fresh data stored in dataframe

fresh_data = base_data[['id']]
fresh_data = fresh_data.merge(crypto_data, on='id', how='left')

# Calculating the Fisher price index

def index_level():

#  Returns the value of the index

	def laspeyres_index():

		# Calculates the Laspeyres price index

		laspeyres_numerator = (base_data['weight'] * fresh_data['price'] * base_data['supply']).sum()
		laspeyres_denominator = (base_data['weight'] * base_data['price'] * base_data['supply']).sum()
		laspeyres = laspeyres_numerator / laspeyres_denominator * 100

		return laspeyres

	def paasche_index():

		# Calculates the Paasche price index

		paasche_numerator = (base_data['weight'] * fresh_data['price'] * fresh_data['supply']).sum()
		paasche_denominator = (base_data['weight'] * base_data['price'] * fresh_data['supply']).sum()
		paasche = paasche_numerator / paasche_denominator * 100

		return paasche

	def fisher_index():

		# Calculates the Fisher index

		laspeyres = laspeyres_index()
		paasche = paasche_index()
		fisher = np.sqrt(laspeyres * paasche)

		return fisher

	return fisher_index()



# Loading previous index values

index_levels = pd.read_csv('index_levels.csv', index_col=0)

# Variables to help store the fresh index value

today = date.today()
index_now = index_level()

next_row = {'Date':today, "Index":index_now}


# Adding the new value to the file and saving it

index_levels = index_levels.append(next_row, ignore_index=True)

index_levels.to_csv(r'index_levels.csv')