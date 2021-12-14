# Lohikäärmien maailma

Sovellus on yhden pelaajan peli

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/vaatimusmaarittelu.md)

[Tuntikirjanpito](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/tuntikirjanpito.md)

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
> poetry run invoke test
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
