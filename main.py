import requests
import utils

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

def get_sets(query):
    '''queries the sets and stores a list of all sets ids and card numbers'''
    params = {
        'q': query,
        'orderBy': 'releaseDate'
    }

    endpoint = 'sets/'
    url = base_uri + endpoint
    response = requests.get(url, params=params, headers=headers).json()['data']
    list_of_sets = [(set_['id'], set_['total']) for set_ in response]
    return list_of_sets

list_of_sets = get_sets('')

