import csv

filename = 'henkiloautot-sahko-merkit.csv'

csv_file = open(filename)
reader = csv.reader(csv_file)
headers = next(reader)
rows = []
for row in reader:
    rows.append(row)
csv_file.close()

years = range(2016, 2022)

counts = {}  # make empty dictionary for yearly counts

for row in rows:
    if row[1] == '':
        continue
    year = int(row[1][:4])
    if year not in years:
        continue
    if year not in counts:
        counts[year] = 0
    counts[year] += 1

print(f'Sähköautojen ensirekisteröinnit {years.start} - {years.stop - 1}')
for year in years:
    print(f'{year}: {counts[year]:>5}')
print(f'Yhteensä: {len(rows)}')
