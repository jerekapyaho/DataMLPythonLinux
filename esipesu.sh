# Irrotetaan ensin kaikki autot joissa on käyttövoimana sähkö
echo "Etsitään sähköautoja"
csvgrep -d ";" -c 19 -m "04" -e iso-8859-1 \
	TieliikenneAvoinData_5_18.csv >sahkoautot.csv

# HUOM.! csvgrep muuntaa erotinmerkin pilkuksi, joten -d-optiota
# ei enää tarvita seuraavissa vaiheissa.

echo "Etsitään henkilöautoja"
# Erotellaan sitten kaikki henkilöautot (ajoneuvoluokka M1 tai M1G)
csvgrep -c 1 -m "M1" sahkoautot.csv >henkiloautot-sahko.csv

# Lopuksi otetaan mukaan vain sarakkeet 1, 2, 19 ja 26
# ja heitetään muut pois
echo "Siivotaan turhat pois"
csvcut -c 1,2,19,26 henkiloautot-sahko.csv >henkiloautot-sahko-merkit.csv

wc -l henkiloautot-sahko-merkit.csv
