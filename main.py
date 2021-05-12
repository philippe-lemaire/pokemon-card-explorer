import requests
import os
import utils
import csv

api_file = 'api-key/key'

my_key = utils.get_file_contents(api_file)
headers = {'X-Api-Key': my_key}

base_uri = 'https://api.pokemontcg.io/v2/'

def get_cards(query):
    '''takes a query and returns a list of cards as dicts'''
    params = {
        'q': query,
        'page': 1,
        #'pageSize': pageSize,
        ' orderBy': 'hp'
    }
    
    endpoint = 'cards/'
    url = base_uri + endpoint
    response = requests.get(url, params=params, headers=headers).json()['data']
    return response

sets = ['set.id:sm1']

for index, item in enumerate(sets):
    cards = get_cards(item)

for card in cards:
    name = card['name']
    supertype = card['supertype']
    print(f"{name} is a {supertype} card")




