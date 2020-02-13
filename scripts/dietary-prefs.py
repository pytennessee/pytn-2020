import collections
import csv

prefs = collections.Counter()
others = []
with open('questions.csv', 'r') as f:
    reader = csv.DictReader(f)

    for row in reader:
        if row['Ticket Type'] in ('Swag Package', 'Donation - Not for Admission'):
            continue

        restriction = row['Do you have any dietary restrictions?']

        if restriction == 'Other':
            others.append(row['Please give us some more info about your restriction so we can do our best to accommodate it!'])

        prefs[restriction] += 1

for restriction, count in prefs.items():
    print(f'{restriction}: {count}')

print('\nOthers')
print('------')
for other in others:
    print(f'* {other}')
