# Lihikäärmien maailma

Sovellus on yhden pelaajan peli

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/vaatimusmaarittelu.md)

[Tuntikirjanpito](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/tuntikirjanpito.md)
[Testaus]()

## Asennus

1. Asenna riippuvuudet komennolla:

>poetry install

2. Käynistä sovellus komennolla: 

> poetry run invoke start

## Koentorivitoiminnot

### Ohjelmanan suorittaminen

Ohjelman pystyy suorittamaan komennolla:

> poetry run invoke start 

### Testaus

Testit suoritetaan komennolla:

> poetry run invoke test

### Testikattavuus

Testikattavuusraportin voi generoida komennolla: 

>poetry run invoke coverage-report

Raporti generoituu **htmlcov**-hakemistoon

