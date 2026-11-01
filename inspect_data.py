def inspect_column(filename, column):

    import csv
    ## Read the file
    with open(filename, encoding='utf-8-sig') as file:
        rows = list(csv.DictReader(file))
    values = []

    ## Iterate on a given column and clean it
    for row in rows:
        value = float(row[column].strip())
        if value == '':
            continue
        values.append(value)
        ## Retuurn the summary of the given column
    return{
            'Count of Value': len(values),
            'Smallest Value': min(values),
            'Highest Value': max(values) ,
            'Average': sum(values) / len(values)
    }

exposed_settlement_area = inspect_column('my-project/data/processed/flood_exposed_settlement.csv', 'exposed_area_km2')
total_settlement_area = inspect_column('my-project/data/processed/flood_exposed_settlement.csv', 'total_area_km2')

print(f'Exposed Settlement Area: {exposed_settlement_area}')
print(f'Total Settlement Area: {total_settlement_area}')


