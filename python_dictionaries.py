## Reading a CSV Properly

import csv
import json
with open('wards.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row);
        print(row['ward'], row['area_km2'])

'''
with open('data.json', encoding='utf-8-sig') as f:
    data = json.load(f)
    print(data['name'])
####
'''

## Handling Messy and Missing data

with open('wards.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        raw = row['area_km2'].strip() #remove the spaces around the value
        if raw == '':
            continue #if raw is an empty string skip and move to the next iteration
        area = float(raw)
        print(raw)

### NOTES

## encoding='utf-8-sig'
'''
Removes the invisible BOM (Byte Order Mark)
sometimes added to CSV files exported from Excel or QGIS.
This prevents issues when accessing column names.
'''

## csv.DictReader() 
'''
csv.DictReader(): Reads a CSV file and converts each row
into a Python dictionary, using the column headers as keys.
e.g {'name': 'Bodija', 'area': '8.1', 'lga': 'Ibadan North'}
'''

## json.load() 

'This is used to read json file and and return it back as an ordinary python dictionary'