import csv

filename = 'henkiloautot-sahko-merkit.csv'

all_rows = []

csv_file = open(filename, encoding='iso-8859-1')
reader = csv.reader(csv_file)
headers = next(reader)
for row in reader:
    if row[0] in ['M1', 'M1G']:
        all_rows.append(row)
csv_file.close()

print(len(all_rows))

years = range(2016, 2023)
counts = {}
for row in all_rows:
    if row[1] == '':  # ohita tyhjä rek. pvm
        continue
    year = int(row[1][:4])  # irrota rek. vuosi
    if year < years.start:  # ohita liian vanha
        continue
    if year not in counts:  # tee uusi lista vuodelle
        counts[year] = [0] * 12
    month = int(row[1][5:7]) - 1  # irrota rek. kuukausi
    counts[year][month] += 1

print(f'Sähköautojen ensirekisteröinnit {years.start} - {years.stop - 1}')
for year in years:
    print(f'{year}: {sum(counts[year]):>5}')
    for month in range(12):
        print(f'\t{month+1:>2}: {counts[year][month]}')
print(f'Yhteensä: {len(all_rows)}')

import matplotlib.pyplot as plt

labels = []
values = []
for year in years:
    for month in range(12):
        labels.append(f'{year}\n-{month+1}')
        values.append(counts[year][month])

plt.bar(labels, values, tick_label=labels)
plt.show()
