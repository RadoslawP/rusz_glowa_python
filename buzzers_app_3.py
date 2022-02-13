import csv

with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)
