import pprint
from datetime import datetime


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    more_dests = []
    more_dests = [dest.title() for dest in flights.values()]

pprint.pprint(more_dests)
print()


more_flights = {}
more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}

pprint.pprint(more_flights)


wests = []
for k, v in fts.items():
    if v == 'West End':
        wests.append(k)

wests_2 = [k for k, v in fts.items() if v == 'West End']

print(wests)
print(wests_2)
