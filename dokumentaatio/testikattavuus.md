# Testausdokumentti

Ohjelma on testattu sekä automatisoiduin yksikköteistein sekä manualisesti tapahtunein järjestelmätason testein.

## Testikattavuus

Käyttöliittymäkerrosta lukuunottamatta sovelluksen testauksen haarautumakattavuus on 97%

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti

### Asennus ja konfigurointi

Sovellus on haettu ja sitä on testattu [käyttöohjeiden]()kuvaamalla tavalla Linux-ympäristöön.

### Toiminnallisuudet

Kaikki [määrittelydokumentin]() ja käyttöohjeiden listaamat toiminnaliisuudet on käyty läpi. Kaikkijen toiminnallisuuksien yhteydessä on syötekentät yritetty täyttää myös virheellisillä arvoilla, kuten tyhjillä

## Sovellukseen jääneet laatuongelmat

- SQLite tietokantaa ei ole alustettu, eli `python -m poetry run invoke build`-komentoa ei ole suoritettu