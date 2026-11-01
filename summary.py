import csv

def read_rows(filename):
    with open(filename, encoding='utf-8-sig') as file:
        rows = list(csv.DictReader(file))
        return rows

def clean_values(rows, column):
    values = []
    for row in rows:
        value = row[column].strip()
        if value == '':
            continue
        values.append(float(value))
    return values

def summarise(values):
    if len(values) == 0:
        return {'Count': 0, 'Smallest' : None, 'Largest': None, 'Average': None}
    
    return{
            'Count of Value': len(values),
            'Smallest Value': min(values),
            'Highest Value': max(values) ,
            'Average': sum(values) / len(values)
    }

def summarise_all(filename, columns):
    rows = read_rows(filename);
    report = {};
    for column in columns:
        values = clean_values(rows, column)
        report[column] = summarise(values)
    return report

rows = read_rows('my-project/data/processed/flood_exposed_settlement.csv');
values = clean_values(rows, 'total_area_km2')
result = summarise(values)


report = summarise_all('my-project/data/processed/flood_exposed_settlement.csv', ['exposed_area_km2','total_area_km2'])

for column, stats in report.items() :
    print(column, ' ->', stats)
