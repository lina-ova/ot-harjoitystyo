# Lohikäärmien maailma

Sovellus on yhden pelaajan peli. Sovellus on Lohikäärmien maailma peli. Tässä pelissa pelaaja on maassa, joka on täynnä lohikäärmeitä ja aarteita. Kaikki lohikäärmeet asuvat luolissa ja niillä on suuria kasoja aarteita. Pelaaja kerää aarteet. Lohikäärme voi syödä pelaajan, viedä pelaajan rahaa tai syödä sen. Jos Pelaaja tulee syödyksi, hän voi yrittää pelastua suorittamalla tehtävän. Pelaaja voi katsoa muiden suorituksia ja ennen pelistä lähtöä tallentaa omaa suoritusta.

## Dokumentaatio

[Käyttöohje](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/vaatimusmaarittelu.md)

[Arkitehtuurikuvaus](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/arkitehtuuri.md)

[Testausdokumentti](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/testikattavuus.md)

[Tuntikirjanpito](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Taustakuvien lähteet](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/background_kuvien_lahteet.md)

## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelmanan suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla

```bash
poetry run invoke coverage-report
```

Raporti generoituu **htmlcov**-hakemistoon

## Pylint

Tidoston [.pylintrc](./.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
