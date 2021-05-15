import csv
import requests
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
    '''queries the sets and stores a list of all sets ids and card numbers'''
    params = {
        'q': query,
        'orderBy': 'releaseDate'
    }

    endpoint = 'sets/'
    url = base_uri + endpoint
    response = requests.get(url, params=params, headers=headers).json()['data']
    return response

def write_to_csv(items):
    '''writes a list of sets (as dicts) to a csv file in the data/ dir'''
    with open('data/sets.csv', 'w') as csv_file:
        fieldnames = items[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in items:
            writer.writerow(row)
