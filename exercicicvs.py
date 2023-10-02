
# extract

import csv


csv_filename = 'basket_players.csv'

with open(csv_filename) as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)


# transform

