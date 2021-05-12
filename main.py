import requests
import os
import utils

api_file = 'api-key/key'

my_key = utils.get_file_contents(api_file)

base_uri = 'https://api.pokemontcg.io'

