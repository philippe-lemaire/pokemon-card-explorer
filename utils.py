import csv

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


def write_csv(series, cards):
    '''takes a pokemon series such as 'sun and moon' and a list of dicts representing cards
    and write a csv file for it in the cards folder'''
    with open(f"cards/{series}.csv", 'w') as csv_file:
        writer = csv.DictWriter(csv_file, cards[2].keys())
        writer.writeheader()
        for card in cards:
            writer.writerow(card)