# DataMLPythonLinux

Kurssimateriaalia ja esimerkkejä data-analyysin projektikurssilla.

## Työkalut

Ohjeet ovat enimmäkseen Ubuntu Linuxille. Useimmat ohjelmistot asennetaan
`apt-get`-työkalulla.

* [csvkit](https://csvkit.readthedocs.io/en/latest/) (asennus esim.
`sudo apt-get install csvkit`)
* [curl](https://curl.se/) (todennäköisesti on jo mukana Linux-asennuksessa)

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
  
## Traficomin avoin data

Ajoneuvotiedot ovat [Traficomin avointa dataa](https://www.traficom.fi/fi/ajankohtaista/avoin-data?toggle=Ajoneuvojen%20avoin%20data).

## Sähköautojen ensirekisteröintien kehitys

Erottele Traficomin ajoneuvodatasta tarvittavat sarakkeet
komentojonolla `esipesu.sh`:

    bash esipesu.sh

Keräile rekisteröintitiedot vuosilta 2016-2021 Python-ohjelmalla
`ev_counts.py`. Varmista, että esipesun tuottama tiedosto on
samassa hakemistossa, ja aja sitten ohjelma:

    python3 ev_counts.py

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
