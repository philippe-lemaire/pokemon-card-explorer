import csv
import requests
import pandas as pd
import os

api_file = 'api-key/key'

base_uri = 'https://api.pokemontcg.io/v2/'

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

my_key = get_file_contents(api_file)
headers = {'X-Api-Key': my_key}


def get_sets(query):
    '''queries the sets and stores a list of all sets'''
    params = {
        'q': query,
        'orderBy': 'releaseDate'
    }
    endpoint = 'sets/'
    url = base_uri + endpoint
    response = requests.get(url, params=params, headers=headers).json()['data']
    return response


def search_cards(query):
    '''returns a list of cards (as dicts) based on the query'''
    params = {
        'q': query,
        'orderBy': 'releaseDate'
    }
    endpoint = 'cards/'
    url = base_uri + endpoint
    response = requests.get(url, params=params, headers=headers).json()['data']
    return response


def save_search_to_pickle(items, filename):
    '''writes a search result list to data/filename.csv'''
    df = pd.DataFrame(items)
    df.to_pickle(path=f'data/{filename}.pickle')
    
def download_cards(query, download_images=False):
    '''takes a query, fetches card data, saves it as csv, and fetches all the hi-res images'''
    card_list = search_cards(query)
    save_search_to_pickle(card_list, query[7:])
    if download_images:
        os.makedirs(f"data/img/{query[7:]}",exist_ok=True)
        for card in card_list:
            print(f"{card['name']} is being downloaded.")
            r = requests.get(url=card['images']['large'], headers=headers)
            open(f"data/img/{query[7:]}/{card['id']}-{card['name']}.png", 'wb').write(r.content)