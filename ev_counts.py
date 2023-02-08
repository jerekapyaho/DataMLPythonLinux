import csv

filename = 'henkiloautot-sahko-merkit.csv'

csv_file = open(filename)
reader = csv.reader(csv_file)
headers = next(reader)
rows = []
for row in reader:
    rows.append(row)
csv_file.close()

years = range(2016, 2023)

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

# Tee ennen tätä virtuaaliympäristö samaan hakemistoon
# missä projekti on: `python3 -m venv venv`.
# Aktivoi virtuaaliympäristö: `source venv/bin/activate`
# Asenna sitten Matplotlib: `pip install matplotlib`.
# Kun olet lopettanut projektin työstämisen, 
# anna komento `deactivate`.
 
import matplotlib.pyplot as plt

values = [counts[k] for k in sorted(list(counts.keys()))]
plt.bar(sorted(list(counts.keys())), values, 
    tick_label=sorted(list(counts.keys())))
plt.show()
