echo "*** Kopioidaan alkuperäinen tiedosto käsiteltäväksi tiedostoksi"
cp -v Ajoneuvojen_avoin_data_5_21.csv ajoneuvot-original.csv

file ajoneuvot-original.csv
file -i ajoneuvot-original.csv

echo "*** Muunnetaan rivinvaihdot Unix-tyylisiksi"
dos2unix -v -n ajoneuvot-original.csv ajoneuvot-unix.csv

echo "*** Muunnetaan merkistökoodaus UTF-8:ksi"
iconv -f iso-8859-1 -t utf-8 ajoneuvot-unix.csv >ajoneuvot-unix-utf8.csv

echo "*** Siivotaan väliaikaiset tiedostot"
mv ajoneuvot-unix-utf8.csv ajoneuvot.csv
rm ajoneuvot-unix.csv
rm ajoneuvot-original.csv

ls -goh --time-style=long-iso ajoneuvot.csv
wc -l ajoneuvot.csv
