# Käyttöohje

Lataa projectin viimeisimmän releasen lähdekoodi valitsemalla _Asserts_-osion alta _Source code_.

## Ohjelman käynistäminen

Ennen ohjelman käynistämistä, asenna riippuvuudet komennolla:

```bash
poetry install
```

Jonka jälkeen suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

Nyt ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Pelin aloittaminen

Sovellus käynistyy aloitusnäkymään: 

Pelin aloittaminen onnistuu painaamalla "Enter the Dragon Realm" painoketta.. Pelaaja siirtyy pelinäkymään

Muiden pelaajien teitojen katseleminen onnisuu painaamalla "Show History of Treasure Hunters. Pelaaja siirtyy History näkymään

## History

Tässä näkymässä pelaaja näkee kolmen parhaan pelaajan tulokset. 

Muiden pelaajien tiedot voi etsiä kirjoittamalla pelaajan nimi tekstikentään ja varmistamalla valinnan painaamalla "Search for hunter in history" painiketta. 

Painaamalla "close the book of hunters painiketta pelaaja palaa Aloitusnäkymään 

## Pelaaminen

Pelinäkymässä: 

On mahdollista valita kahden luolan välissä painaamalla yhden "Cage 1" ja "Cage 2" painikkeista. 

Painaaminen vie käyttäjää yhteen tulosnäkymistä:

## Voitto

Tulosnäkymässä näen minkä verran aarteita olet saanut ja tämänhetkinen aarretilanne. 

Painaamalla "Go Further" Painiketta pelaaja jatkaa pelia ja palaa Pelinäkymään.

Painaamalla "Exit the realm..." painiketta pelaaja osoittaa haluttaan poistua pelista. Ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.


Painaamalla "yes Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

## Häviö

Tulosnäkymässä näen minkä verran aarteita olet hävinny ja tämänhetkinen aarretilanne. 

Painaamalla "Go Further" Painiketta pelaaja jatkaa pelia ja palaa Pelinäkymään.

Painaamalla "Exit the realm..." painiketta pelaaja osoittaa haluttaan poistua pelista. Ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.

Painaamalla "yes Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

## Kuolema

Kuolema tulosnäkyvästä pelaaja voi lopettaa pelin painaamalla "Go to the afterworld" painiketta. 

Ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.
Painaamalla "yes Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

Pelaaja voi myös yrittää pelastua painaamalla "Try to survive?" painiketta. Tällöin aukeaa Tehtävän suorittamisen näkymää.

## Tehtävän suorittaminen 

Näkymässä pelaaja näkee hänelle annettu tehtävä. Vastaus on kirjoitettavaa tekstikenttään. 

Vastaus on kirjoitettava yhdellä sanalla, pienillä kirjaimillä, ilman välilyöntejä. Jos tehtävä on matemaattinen, vastaus on kirjoitettava numeroina. 

Painaamalla "Try to survive" painiketta pelaaja vahvistaa vastauksen ja siirtyy seuraavaan näkymään.

## Oikea Vastaus

Jos Pelaaja vastaa oikein, hän näkee seuraavan näkymän:

Näkymästä voi lopettaa pelin painaamalla "Exit..." painiketta.
 Tuolloin ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.
Painaamalla "yes Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

"Go further" painike vie pelaaja Pelinäkymään

## Väärä vastaus

Jos pelaaja vastaa väärin, hän näkee seuraavan näkymän:

Tästä pelaaja voi vain lopettaa pelin painaamalla "go to the afterworld" painiketta 

Tuolloin ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.
Painaamalla "yes Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

## Tietojen tallentaminen

Jos pelaaja jossain vaiheessa pelia varmistaa, että haluaa lähteä pelistä ja tallentaa tietojaan, hän näkee seuraavan näkymän 

"Treasures" ilmoittaa pelaajan tämän hetken mennessä kerättyjen aarteiden määrä ja Status siitä, onko pelaaja elossa vai kuollut

Oman nimen voi kirjoittaa tekstikenttään. 
Nimen valinta vahvistetaan painaamalla painaamalla "Write the name painiketta". 
Jos valittu nimi on jo varattu pelaaja palautetaan samaan näkymään, jossa hän voi vaihtaa nimen. 
Jos nimi on vapaa, ohjelma varmistaa pelaajalta, että se on se nimi, jolla hänet muistetaan. Sen jälkeen ohjelma sulkeutuu

Painaamalla "Stay unknown" pelaaja varmistaa, ettei haluakaan tallentaa tietojaan. Sen jälkeen ohjelma sulkeutuu.