def inspect_column(filename, column):

    import csv
    with open(filename, encoding='utf-8-sig') as file:
        rows = list(csv.DictReader(file))
    values = []

    for row in rows:
        value = float(row[column].strip())
        if value == '':
            continue
        values.append(value)
    return{
            f'Smallest Value: {min(values)}',
            f'Highest Value: {max(values)}',
            f'Count of Value: {len(values)}'
    }

total_settlement_area = inspect_column('my-project/data/processed/flood_exposed_settlement.csv', 'total_area_km2')
exposed_settlement_area = inspect_column('my-project/data/processed/flood_exposed_settlement.csv', 'exposed_area_km2')

print(f'Total Eti-Osa Settlement area: {total_settlement_area}');
print(f'Exposed Eti-Osa Settlement area: {exposed_settlement_area}')

