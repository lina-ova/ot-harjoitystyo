# Arkitehtuurikuvaus

## Rakenne 

Pakkaus _ui_ sisältää käyttöliittymää
Pakkaus _background_ sisältää tauskakuvia
Pakkaus _data_ sisältää tietokannan tauluja alustavia käskyjä
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

Jokainen näistä on toteutettu omana luokanaan. Näkymistä yksi on aina kerrallaan näkyvänä. Näkymän näyttämisestä vastaa UI-luokka. Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. On pyritty käyttämään _define_ pakkauksen luokkia. Tieto pelaajan rahatielanteesta tallennetaan kuitenkin UI-luokkaan, koska pelaajalle ei pyritty luomaan omaa luokkaa yhden atribuutin takia. 

## Sovelluslogiikka

## Tietojen pysyväistallennus

Pakkauksen _define luokka `Hunters` huolehtii pelaajan tietojen tallentamisesta. Luokka tallentaa tietoa SQLITE-tietokantaan.

Luokka `DefineTask` vastaa pelaajalle annettavan tehtävän hakemisesta tietokannasta, luokka ei tallenna mitään tietokantaan 

## Päätoiminnallisuudet

Kuvataan seuraavaksi sovelluksen toimintalogiikka muutaman päätoiminnallisuuden osalta sekvenssikaaviona

## Ohjelman rakenteeseen jääneet heikkoudet

### Käyttöliittymä

Graafisen käyttöliittymän koodissa on jonkin verran toisteisuutte, jota voisi toteuttaa omia komponenttejaan. Esimerkiksi pylint ilmoittaa toisteista koodissa luokissa `SurviveDigestView` ja `Result`
