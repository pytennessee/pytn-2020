import collections
import csv


stats = collections.Counter()
shirt_count = collections.Counter()
vol_shirt_count = collections.Counter()
with open('questions.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        size = row['T-shirt size']
        ticket = row['Ticket Type']
        if ticket == 'Swag Package' and not size:
            name = row['First Name'] + ' ' + row['Last Name']
            print(f'{name} bought Swag with no size info')
        if size:
            if ticket == 'Volunteer':
                vol_shirt_count[size] += 1
            else:
                shirt_count[size] += 1
            stats[ticket] += 1

print('\nAttendee Shirts')
print('---------------')
for size, count in shirt_count.items():
    print(f'{size}: {count}')

print('\nVolunteer Shirts')
print('---------------')
for size, count in vol_shirt_count.items():
    print(f'{size}: {count}')

print ('\nStats')
print ('-----')
for ticket, count in stats.items():
    print(f'{ticket}: {count}')

attendee_shirts = sum(shirt_count.values())
volunteer_shirts = sum(vol_shirt_count.values())
total = attendee_shirts + volunteer_shirts
print(f'\nTotal: {total} ({attendee_shirts} attendees, {volunteer_shirts} volunteers)')

