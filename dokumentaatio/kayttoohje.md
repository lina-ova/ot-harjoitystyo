# Käyttöohje

Lataa projectin viimeisimmän [releasen](https://github.com/lina-ova/ot-harjoitystyo/releases) lähdekoodi valitsemalla _Asserts_-osion alta _Source code_.

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

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/hello_view.png)

Pelin aloittaminen onnistuu painaamalla "Enter the Dragon Realm" painoketta.. Pelaaja siirtyy pelinäkymään

Muiden pelaajien teitojen katseleminen onnisuu painaamalla "Show History of Treasure Hunters. Pelaaja siirtyy History näkymään

## History

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/history.png)

Tässä näkymässä pelaaja näkee kolmen parhaan pelaajan tulokset. 

Muiden pelaajien tiedot voi etsiä kirjoittamalla pelaajan nimi tekstikentään ja varmistamalla valinnan painaamalla "Search for hunter in history" painiketta. 

Painaamalla "close the book of hunters" painiketta pelaaja palaa Aloitusnäkymään 

## Pelaaminen

Pelinäkymässä: 

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/play_view.png)

On mahdollista valita kahden luolan välissä painaamalla yhden "Cage 1" ja "Cage 2" painikkeista. 

Painaaminen vie käyttäjää yhteen tulosnäkymistä:

## Voitto

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/win_view.png)

Tulosnäkymässä näen minkä verran aarteita olet saanut ja tämänhetkinen aarretilanne. 

Painaamalla "Go Further" Painiketta pelaaja jatkaa pelia ja palaa Pelinäkymään.

Painaamalla "Exit the realm..." painiketta pelaaja osoittaa haluttaan poistua pelista. Ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/question.png)

Painaamalla "yes" Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

## Häviö

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/loss.png)

Tulosnäkymässä näen minkä verran aarteita olet hävinny ja tämänhetkinen aarretilanne. 

Painaamalla "Go Further" Painiketta pelaaja jatkaa pelia ja palaa Pelinäkymään.

Painaamalla "Exit the realm..." painiketta pelaaja osoittaa haluttaan poistua pelista. Ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/question.png)

Painaamalla "yes" Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

## Kuolema

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/gobbled_view.png)

Pelaaja yrittää pelastua painaamalla "Try to survive?" painiketta. Tällöin aukeaa Tehtävän suorittamisen näkymää.

Kuolema tulosnäkyvästä pelaaja voi lopettaa pelin painaamalla "Go to the afterworld" painiketta. 

Ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/question.png)

Painaamalla "yes" Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

## Tehtävän suorittaminen

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/task_view.png)

Näkymässä pelaaja näkee hänelle annettu tehtävä. Vastaus on kirjoitettavaa tekstikenttään. 

Vastaus on kirjoitettava yhdellä sanalla, pienillä kirjaimillä, ilman välilyöntejä. Jos tehtävä on matemaattinen, vastaus on kirjoitettava numeroina. 

Painaamalla "Try to survive" painiketta pelaaja vahvistaa vastauksen ja siirtyy seuraavaan näkymään.

## Oikea Vastaus

Jos Pelaaja vastaa oikein, hän näkee seuraavan näkymän:

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/survived_view.png)


"Go further" painike vie pelaaja Pelinäkymään

Näkymästä voi lopettaa pelin painaamalla "Exit..." painiketta.
Tuolloin ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.
 
 ![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/question.png)
 
Painaamalla "yes" Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

## Väärä vastaus

Jos pelaaja vastaa väärin, hän näkee seuraavan näkymän:

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/digested_view.png)

Tästä pelaaja voi vain lopettaa pelin painaamalla "go to the afterworld" painiketta 

Tuolloin ohjelma kysyy pelaajalta, jos haluaa tallentaa tulostaan ennen lähtöä.

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/question.png)

Painaamalla "yes" Pelaaja siirtyy Tietojen tallentamiseen näkymään. Painaamalla "No" pelaaja sulkee pelin.

## Tietojen tallentaminen

Jos pelaaja jossain vaiheessa pelia varmistaa, että haluaa lähteä pelistä ja tallentaa tietojaan, hän näkee seuraavan näkymän: 

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/write_view.png)

"Treasures" ilmoittaa pelaajan tämän hetken mennessä kerättyjen aarteiden määrä ja Status siitä, onko pelaaja elossa vai kuollut

Oman nimen voi kirjoittaa tekstikenttään. 

Nimen valinta vahvistetaan painaamalla painaamalla "Write the name painiketta". 

Jos valittu nimi on jo varattu pelaaja palautetaan samaan näkymään, jossa hän voi vaihtaa nimen. 

Jos nimi on vapaa, ohjelma varmistaa pelaajalta, että se on se nimi, jolla hänet muistetaan. Sen jälkeen ohjelma sulkeutuu

Painaamalla "Stay unknown" pelaaja varmistaa, ettei haluakaan tallentaa tietojaan. Sen jälkeen ohjelma sulkeutuu, eikä tietoja tallenneta
