import csv

filename = 'henkiloautot-sahko-merkit.csv'

all_rows = []

csv_file = open(filename)
reader = csv.reader(csv_file)
headers = next(reader)
for row in reader:
    if row[0] in ['M1', 'M1G']:
        all_rows.append(row)
csv_file.close()

print(len(all_rows))

years = range(2016, 2027) # nyt on 2026 mukana
counts = {}
for row in all_rows:
    if row[1] == '':
        continue
    year = int(row[1][6:])
    if year < years.start:
        continue
    if year not in counts:
        counts[year] = [0] * 12
    month = int(row[1][3:5]) - 1
    counts[year][month] += 1

# Lisää tyhjä lista myös vuodelle 2026:
counts[years.stop - 1] = [0] * 12

print(f'Sähköautojen ensirekisteröinnit {years.start} - {years.stop - 1}')
for year in years:
    print(f'{year}: {sum(counts[year]):>5}')
    for month in range(12):
        print(f'\t{month+1:>2}: {counts[year][month]}')
print(f'Yhteensä: {len(all_rows)}')

# Regressiomallia varten muista ensin aktivoida
# virtuaaliympäristö, sitten asenna Scikit-Learn:
# `pip install scikit-learn`
# Matplotlibin asennus on jo vetänyt mukaan NumPy-kirjaston. 

import numpy as np
from sklearn.linear_model import LinearRegression

x_arr = []  # 0, 1, 2, ... = 2016-01, 2016-02, 2016-03...
x_val = 0
y_arr = []  # rekisteröintimäärät
leftover_count = 0  # montako kuukautta on vailla dataa
for year in years:
    # Data puuttuu viimeiseltä vuodelta.
    # Se täydennetään ennusteen tuottamalla datalla. 
    if year == 2026:
        leftover_count += 12
        continue
    for month in range(12):
        # Data puuttuu myös v. 2025 lopulta
        if year == 2025 and month >= 9:
            leftover_count += 1
            continue
        x_arr.append(x_val)
        x_val += 1
        y_arr.append(counts[year][month])

# Nyt x_arr sisältää arvot 0...77, missä 0 = tammikuu 2016,
# 1 = helmikuu 2016 jne., ja 116 = syyskuu 2022.
# Yhteensä siis 9 * 12 + 9 = 117 kuukautta.

# y_arr sisältää rekisteröintimäärät 1/2016 ... 9/2025.
print(f'Kuukausia: {len(y_arr)}')
#print(y_arr)

# NumPy-taulukot ovat hieman erilaisia kuin Pythonin listat,
# joten täytyy tehdä pieni muunnos:
x = np.array(x_arr).reshape((-1, 1))
y = np.array(y_arr)

#print(x)
#print(y)

# Seuraava perustuu artikkeliin
# https://realpython.com/linear-regression-in-python/

# Tehdään lineaarinen regressiomalli ja sovitetaan siihen x ja y:
model = LinearRegression()
model.fit(x, y)

r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
print(f"intercept: {model.intercept_}")
print(f"slope: {model.coef_}")

# Ennustetaan x:n perusteella y:n arvot
y_pred = model.predict(x)
#print(f"predicted response:\n{y_pred}")

print(f'Ennustetaan {leftover_count} kuukautta...')
future_x = list(range(x_val, x_val + leftover_count))
x_new = np.array(future_x).reshape((-1, 1))
#print(x_new)
y_new = model.predict(x_new)
print(y_new)
print(type(y_new))

# Keräillään valmiit arvot ja niiden otsakkeet kuviota varten
labels = []
year = years.start
month = 0
values = y_arr
for x in x_arr:
    labels.append(f'{year}-{month+1:>02}')
    month += 1
    if month == 12:
        month = 0
        year += 1

total_count = 0
count_2025 = 0
count_2026 = 0
year = 2025
month = 9
#print(future_x)
for fx in future_x:
    count = int(y_new[fx - len(x_arr)])
    total_count += count
    label = f'{year}-{month+1:>02}'
    labels.append(label)
    values.append(count)  # lisätään ennustettu arvo
    print(f'{label}: {count} *')
    if year == 2025:
        count_2025 += count
    if year == 2026:
        count_2026 += count
    month += 1
    if month == 12:
        month = 0
        year += 1
print(f'Ennuste ajalle 2025-10 - 2025-12: {total_count}')
print(f'Ennuste loppuvuodelle 2025: {count_2025}')
print(f'Ennuste vuodelle 2026: {count_2026}')

import matplotlib.pyplot as plt
print(labels)
print(values)
plt.bar(labels, values, tick_label=labels)
plt.show()
