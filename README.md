# DataMLPythonLinux

Kurssimateriaalia ja esimerkkejä data-analyysin projektikurssilla.

## Työkalut

Ohjeet ovat enimmäkseen Ubuntu Linuxille. Useimmat ohjelmistot asennetaan
`apt-get`-työkalulla.

* [csvkit](https://csvkit.readthedocs.io/en/latest/) (asennus esim.
`sudo apt-get install csvkit`)
* [curl](https://curl.se/) (todennäköisesti on jo mukana Linux-asennuksessa)

## Traficomin avoin data

Ajoneuvotiedot ovat [Traficomin avointa dataa](https://tieto.traficom.fi/fi/tietotraficom/avoin-data).

Datan voi ladata joko selaimella tai suoraan komentoriviltä curl-ohjelmalla,
tallentaen tiedostoon -o-optiolla:

    curl https://opendata.traficom.fi/Content/Ajoneuvorekisteri.zip -o Ajoneuvorekisteri.zip

Verkko-osoite löytyy linkistä Traficomin verkkosivulta.

## Datan siivous

Traficomin ajoneuvodata on CSV-muodossa ja pakattu ZIP-tiedostoon. Pura ZIP-paketti sopivaan
hakemistoon `unzip`-komennolla. Dataan kuuluu myös muuttujien kuvaus, joka on Excel-tiedostossa.
Sitä voi tarkastella Linuxissa esimerkiksi LibreOffice-ohjelmistolla.

Kopioidaan alkuperäinen tiedosto ensin toiselle nimelle, jotta komennoista ei tule niin hankalia (alkuperäinen tiedosto on edelleen saatavissa Traficomin sivuilta ladatussa ZIP-paketissa):

    $ cp Ajoneuvojen_avoin_data_5_30.csv ajoneuvot-original.csv

Käyttämällä file-komentoa voidaan nähdä, että ajoneuvodata on Windows-rivimuodossa 
(eli rivinvaihto on kaksi merkkiä, CR ja LF) ja se käyttää ISO 8859-1 -merkistökoodausta:

    $ file ajoneuvot-original.csv
    ajoneuvot-original.csv: ISO-8859 text, with very long lines (578), with CRLF line terminators

    $ file -i ajoneuvot-original.csv 
    ajoneuvot-original.csv: text/plain; charset=iso-8859-1

Näemmä `file`-ohjelma ei kuitenkaan tunnista tiedostoa CSV:ksi, koska ei ehdota
MIME-tyypiksi `text/csv`.

Ensimmäisessä vaiheessa muunnetaan rivinvaihdot Unix-tyylisiksi
`dos2unix`-ohjelmalla, jonka pitäisi olla valmiiksi käytettävissä Linux-asennuksessa:

    $ dos2unix -v -n ajoneuvot-original.csv ajoneuvot-unix.csv
    dos2unix: Converted 5360982 out of 5360982 line breaks.
    dos2unix: converting file ajoneuvot-original.csv to file ajoneuvot-unix.csv in Unix format...

HUOM. Datan versiossa 5.30 (tai aikaisemminkin) näyttäisi siltä, että rivinvaihdot ovat jo Unix-tyylisiä, joten edellinen vaihe on tarpeeton.

Toisessa vaiheessa muunnetaan ISO 8859-1 -merkistökoodaus UTF-8:ksi käyttäen `iconv`-komentoa:

    $ iconv -f iso-8859-1 -t utf-8 ajoneuvot-unix.csv >ajoneuvot-unix-utf8.csv

Komentojen `-v`- tai `--verbose`-optiot eivät ole välttämättömiä, mutta tässä vaiheessa ne voivat olla
hyödyllisiä (verbose = enemmän selittävää tulostusta, mikä ei Unix-komennoissa
lähtökohtaisesti ole tapana).

Lopputuloksena meillä on kolme CSV-tiedostoa: alkuperäinen, Unix-rivinvaihdoilla varustettu
alkuperäinen sekä vielä UTF-8-merkistöksi muunnettu Unix-rivinvaihdollinen versio:

    $ ls -goh --time-style=long-iso *.csv
    -rw-rw-r-- 1 920M 2024-01-15 11:26 ajoneuvot-original.csv
    -rw-rw-r-- 1 915M 2024-01-15 11:29 ajoneuvot-unix.csv
    -rw-rw-r-- 1 916M 2024-01-15 11:55 ajoneuvot-unix-utf8.csv

Jatkokäsittelyä varten kannattanee nimetä viimeisen vaiheen tiedosto uudelleen:

    $ mv ajoneuvot-unix-utf8.csv ajoneuvot.csv

Tässä repossa oleva skripti `siivous.sh` suorittaa kaikki nämä toiminnot
yhdellä kertaa, ja poistaa vielä lopuksi välivaiheissa syntyneet tiedostot.

## CSVKit ja muita työkaluja

CSV-tiedostojen määritys löytyy [RFC 4180](https://www.ietf.org/rfc/rfc4180.txt):sta.

Tarkastelemalla `ajoneuvot.csv`-tiedostoa `head`-komennolla nähdään, 
että ensimmäinen rivi on otsikkorivi. Tiedosto on CSV-muotoinen, mutta
siinä on käytetty erotinmerkkinä puolipistettä suomalaisen standardin
mukaisesti. Jos jonkin sarakkeen arvoon sisältyy sama erotinmerkki,
niin CSV-määrityksen mukaan sarake pitää sulkea lainausmerkkien sisään.

## Python

Esimerkeissä on käytetty Pythonin versiota 3.10.6. Tarkista oma Python 3-versiosi:

    python3 -V

Pythonin versiota 2 ei kannata enää käyttää uusissa projekteissa.

### Virtuaaliympäristö

Perustietoa Pythonin virtuaaliympäristöistä löytyy esimerkiksi 
Real Python -sivuston artikkelista [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).

Tee projektin hakemistoon uusi virtuaaliympäristö nimeltä `venv`:

    python3 -m venv venv

Komento ajaa Python-moduulin nimeltä `venv` ja luo uuden virtuaaliympäristön.

Aktivoi virtuaaliympäristö:

    source venv/bin/activate

Graafisten kuvaajien tekemistä varten pitää asentaa Matplotlib:

    pip install matplotlib

Lisää tietoa `pip`-ohjelman käytöstä löytyy esimerkiksi Real Python -sivuston
artikkelista [What is Pip](https://realpython.com/what-is-pip/).

Kun olet lopettanut projektin työstämisen, anna komento `deactivate`. Sen jälkeen
`python3`-komento ajaa taas järjestelmän oman Python 3 -tulkin. Aktiivinen 
virtuaaliympäristö näkyy komentokehotteessa, mutta voit tarkistaa tilanteen
komennolla `which python3`.
  

## Sähköautojen ensirekisteröintien kehitys

Erottele Traficomin ajoneuvodatasta tarvittavat sarakkeet
komentojonolla `esipesu.sh`:

    bash esipesu.sh

Keräile rekisteröintitiedot vuosilta 2016-2025 Python-ohjelmalla
`ev_counts.py`. Varmista, että esipesun tuottama tiedosto on
samassa hakemistossa, ja aja sitten ohjelma:

    python3 ev_counts.py

HUOM.! Datan versiossa 5.30 (mahdollisesti jo aikaisemmin) päiväykset ovat
muotoa `PP.KK.VVVV`, joten ohjelma on päivitetty sen mukaisesti. Jos käytät
jotain aikaisempaa datajoukkoa, ota tämä huomioon.

Ohjelma pysyy käynnissä kunnes pylväsdiagrammin sisältävä
ikkuna suljetaan.

HUOM.! Jos saat ilmoituksen:

> UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.

niin ratkaisu on asentaa Tkinter-kirjasto Pythonille:

    sudo apt-get install python3-tk


### Datan pilkkominen vuosimääristä kuukausimääriksi

Ennustemallia varten vuosittaiset sähköautojen rekisteröintimäärät
on pilkottu kuukausittaisiksi Python-ohjelmassa `ev_counts_monthly.py`.

### Ennustemalli käyttäen lineaarista regressiota

Sähköautojen ensirekisteröintimäärät loppuvuodelle 2022 ja koko 
vuodelle 2023 on ennustettu lineaarisen regressiomallin avulla,
käyttäen Scikit-learn-kirjastoa. Tämä versio on tiedostossa
`ev_counts_regression.py`.

Ennustemalli on sovellettu Real Python -sivuston artikkelista
[Linear Regression in Python](https://realpython.com/linear-regression-in-python/).

Aktivoi ensin Python-virtuaaliympäristö ja asenna Scikit-learn:

    source venv/bin/activate
    pip install scikit-learn

Sen jälkeen aja ohjelma:

    python3 ev_counts_regression.py

Tuloksia voi verrata esimerkiksi Tilastokeskuksen tiedotteeseen
[Tammikuussa 2023 ensirekisteröitiin 7 175 uutta henkilöautoa](https://www.stat.fi/julkaisu/cl8cq3s51778x09w2jlxa1tyh).


## Jääkiekkosarjan joukkueiden menestymisen seuranta

Yksi hyvä datan visualisointiharjoitus voisi olla viivadiagrammin piirtäminen
jääkiekkosarjaan osallistuvien joukkueiden sarjasijoituksista kuluvalla sarjakaudella.
Jos käytettävissä on historiatietoa joukkuiden pistemääristä ja ajankohdista, tai
vaikka ottelutiedot, josta nämä voidaan laskea päivän tai vaikka viikon tarkkuudella,
niin pitäisi olla suhteellisen helppoa tehdä Matplotlib-kirjaston avulla viivadiagrammi,
jossa on usean eri muuttujan esitys.

Jos diagrammiin halutaan viikottainen tilanne, niin voidaan vaikka numeroida viikot
sarjakauden alusta, ja sitten kirjata jokaisen viikon sarjasijoitus (tai pistemäärä)
kyseisellä viikolla sopivaan Python-tietorakenteeseen.

Dataa voisi löytyä vaikka [Leijonien](https://tulospalvelu.leijonat.fi/) tai 
[Flashscoren](https://www.flashscore.fi/) verkkosivuilta. Kun ei ole käytössä
rajapintaa, tiedot voidaan keräillä "web scraping" -menetelmällä, mutta se on kovin altis
verkkosivun ajoittaisille muutoksille. Kts. Real Python, 
[A Practical Introduction to Web Scraping in Python](https://realpython.com/python-web-scraping-practical-introduction/).

## Muita avoimen datan lähteitä

* [Digitraffic](https://www.digitraffic.fi/)
* Tampereen [Journeys API](https://wiki.itsfactory.fi/index.php/Journeys_API) / ITS Factory
* [Sotkanet](https://sotkanet.fi/sotkanet/fi/index) / [THL:n avoin data](https://thl.fi/fi/tilastot-ja-data/aineistot-ja-palvelut/avoin-data)
