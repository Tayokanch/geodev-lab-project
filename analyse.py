## STEP 1 : create a ward.csv

"""__________________________________"""

## STEP 2: Read the csv file and count the Lines
with open('wards.csv') as f:
    lines = f.readlines()
print(f'Number of lines {len(lines)}')

print("""__________________________________""")

## STEP 3: Print each line

with open('wards.csv') as f:
    lines = f.readlines() ## The readlines() method reads all line into a list
for line in lines[1:]:
    print(line.strip()); ## The strip() method removes all the invisible new lines to tidy up the output 

print("""__________________________________""")

## STEP 4: Skip the header and split each row

with open('wards.csv') as f:
    lines = f.readlines()
for line in lines[1:]:
    parts = line.strip().split(',')# split(',') splits the string into a list of strings using commas as separators.
    ward = parts[0]
    area = parts[1]
    print(f'{ward} has area {area}')


print("""__________________________________""")

## STEP 5: Convert the area to a number and calculate

with open('wards.csv') as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(',')
    ward = parts[0]
    area_km2 = float(parts[1])
    area_hectares= area_km2 * 100
    print(f'{ward} is {area_hectares} hectares')



"""__________________________________"""

## STEP 6: Add a decision (conditional statement)

with open('wards.csv') as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(',')
    ward = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 9:
        size = 'Large'
    else:
        size = 'Small'
    print(f'ward is {size}')


print("""__________________________________""")
## STEP 7 : Break the code on purpose for error

with open('wards.csv') as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(',')
    ward = parts[0]
    area_km2 = int(parts[1])
    if area_km2 > 9:
        size = 'Large'
    else:
        size = 'Small'
    print(f'ward is {size}')