import csv
import pprint

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.split(',')
        flights[k] = v

pprint.pprint(flights)
