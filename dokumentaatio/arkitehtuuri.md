# Arkitehtuurikuvaus

## Rakenne 

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/rakenne.png)
Pakkaus _ui_ sisältää käyttöliittymää
Pakkaus _background_ sisältää tauskakuvia
Pakkaus _database_ sisältää tietokannan tauluja alustavia käskyjä
Pakkaus _define sisältää luokkia, jotka vuorovaikuttavat tietokannankanssa ja määrettelevät vaihtelevaa näkymän tietoa

## Käyttöliittymä

Käyttöliittymä sisältää useampaa erilaista näkymää

- Alkunäkymä

- Luolanvalinta

- Näkymä, jossa pelaaja on _voittanut/hävinnyt/kuollut_

- Näkymä, jossa pelaaja ratkaisee tehtävän

- Näkymä, jossa pelaaja on pelastunut/kuollut tehtävää suorittaessa

- Näkymä, jossa pelaaja tallentaa tietojaan tietokantaan

- Näkemä jossa pelaaja näkee muiden suorituksia

Jokainen näistä on toteutettu omana luokanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymän näyttämisestä vastaa [UI](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/ui.py)-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. On pyritty käyttämään _[define](https://github.com/lina-ova/ot-harjoitystyo/tree/master/src/define)_ pakkauksen luokkia. Tieto pelaajan rahatielanteesta tallennetaan kuitenkin UI-luokkaan, koska pelaajalle ei pyritty luomaan omaa luokkaa yhden atribuutin takia. 

## Sovelluslogiikka


## Tietojen pysyväistallennus

Pakkauksen _define luokka `Hunters` huolehtii pelaajan tietojen tallentamisesta. Luokka tallentaa tietoa SQLITE-tietokantaan.

Luokka `DefineTask` vastaa pelaajalle annettavan tehtävän hakemisesta tietokannasta, luokka ei tallenna mitään tietokantaan 

## Toiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona


### Pelaajan tietojen tallentaminen

Kun pelaajan 'write to history' näkymässä on syötetty pelaajan keksimä nimi. Sen jälkeen klikataan 'write to history' painiketta, etenee sovelluksen kontrolli seuraavasti

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/write%20to%20history%20.png)

[Tapahtumakäsittelijää](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/ui.py) kutsuu sovelluslogiikan metodia _check_. Funktio välitää käskyn tarkistaa, onko kyseinen nimi varattu _[Hunters](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/define/best_hunters.py)_-lukan olio tarkistaa tietokannasta kyseinen nimi, ja välitää tiedon, onko nimi uniikki vai ei. Jos nimi on Uniikki, [WriteView](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/write_to_hitory_view.py) raise infoboxin, jossa pelaajalta varmistetaan valintansa, myönteisellä vastauksella, pelaajan tiedot välitetään Hunters luokalle kirjoitettavaksi

![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/result.png)

###T ulosnäkymän näyttäminen

[Täpähtumakäsittelijä](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/ui.py) lukee pelaajan painavaan  'Cage 1' tai 'Cage 2' painikeita. 
Pelinäkymä tuhoutuu ja luodaan _[Result](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/win_die_lose_views.py)_-näkymä. 
Result-luokka välittää tiedon pelaajan keräämistä varoista [DefineResult](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/define/define_result.py)-luokalle.
luokka määrittää näkymän, palauttaa tiedon valitusta näkymästä Result-luokalle, tiedon mukaan Result alustaa *_initialize_win* *initialize_lose* tai _initialize_die* näkymät, jotka sitten hakevat tietoja voitosta ja häviöstä  luokasta DefineResult, jos pelaaja on voittanut tai hävinnyt.
Kun kaikki on alustettu, näytetään näkymän pelaajalle

###Surviving 

Kun pelaaja on kuollut pelissa, hänelle ehdotetaan yritää pelastua. Jos pelaaja painaa 'Try to survive' painiketta suoritaan seuraavat toimeet:
![](https://github.com/lina-ova/ot-harjoitystyo/blob/master/dokumentaatio/kuvat/surviving.png)

[Täpähtumakäsittelijä](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/ui.py) lukee pelaajan painaavan painiketta. 
edellinen näkymä tuhoutuu. 
Tapahtumakäsittelijä avaa uuden näkymän. _[Surviving](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/surviving_view.py).Surviving-luokka luo uuden _[SurviveTask](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/define/survivetask.py)-olion, joka vastaa vurovaikuttamisesta tietokannan kanssa. 
SurviveTask generoi tehtävännumeron ja hakee tehtävän ja vastatuksen tietokannsta. ja palauttaa tiedon Surviving näkymälle. Näkymä näytetään pelaajalle.

## Muut toiminnaliisuudet

Sama periaate toistoo sovelluksen kaikissa toiminnallisuuksissa, käyttöliittymän tapahtumakäsittelijä kutsuu sopivaa sovelluslogiikan metodia.

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

Graafisen käyttöliittymän koodissa on jonkin verran toisteisuutte, jota voisi toteuttaa omia komponenttejaan. Esimerkiksi pylint ilmoittaa toisteista koodissa luokissa [SurviveDigestView](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/digest_survive.py) ja [Result](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/write_to_hitory_view.py). Myös luokalle _[Result](https://github.com/lina-ova/ot-harjoitystyo/blob/master/src/ui/win_die_lose_views.py)_ välitetään aika paljon riippuvuuksia, kannattaa siitä varmaan jakaa pienempiin luokkiin
