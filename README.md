# DataMLPythonLinux

Kurssimateriaalia ja esimerkkejä data-analyysin projektikurssilla.

## Työkalut

Ohjeet ovat enimmäkseen Ubuntu Linuxille. Useimmat ohjelmistot asennetaan
`apt-get`-työkalulla.

* [csvkit](https://csvkit.readthedocs.io/en/latest/)

## Traficomin avoin data

Ajoneuvotiedot ovat [Traficomin avointa dataa](https://www.traficom.fi/fi/ajankohtaista/avoin-data?toggle=Ajoneuvojen%20avoin%20data).

## Sähköautojen ensirekisteröintien kehitys

Erottele Traficomin ajoneuvodatasta tarvittavat sarakkeet
komentojonolla `esipesu.sh`.

Keräile rekisteröintitiedot vuosilta 2016-2021 Python-ohjelmalla
`ev_counts.py`.

### Datan pilkkominen vuosimääristä kuukausimääriksi

Ennustemallia varten vuosittaiset sähköautojen rekisteröintimäärät
on pilkottu kuukausittaisiksi Python-ohjelmassa `ev_counts_monthly.py`.

### Ennustemalli käyttäen lineaarista regressiota

Sähköautojen ensirekisteröintimäärät loppuvuodelle 2022 ja koko 
vuodelle 2023 on ennustettu lineaarisen regressiomallin avulla,
käyttäen Scikit-learn-kirjastoa. Tämä versio on tiedostossa
`ev_counts_regression.py`.

Tuloksia voi verrata esimerkiksi Tilastokeskuksen tiedotteeseen
[Tammikuussa 2023 ensirekisteröitiin 7 175 uutta henkilöautoa](https://www.stat.fi/julkaisu/cl8cq3s51778x09w2jlxa1tyh).

