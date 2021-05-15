import utils
sets = utils.get_sets('')
utils.write_to_csv(sets)

dragons = utils.search_cards('supertype:pokemon types:dragon')

utils.write_to_csv(dragons)