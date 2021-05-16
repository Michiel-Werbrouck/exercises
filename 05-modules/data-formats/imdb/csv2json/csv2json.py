import json
import csv
import sys

filename = sys.argv[1]

with open(filename, 'r') as csvfile:
    data = list(csv.DictReader(csvfile))

print(json.dumps(data))