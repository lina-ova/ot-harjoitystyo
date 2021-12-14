from database_connection import get_database_connection

class Hunters:
    """Luokka, joka vastaa:
    pelaajien tietojen tallentamisesta tietokantaan
    ja hakimiesesta tietokannasta"""
    def __init__(self):
        """ Automaattisesti luoma tietokantayhteyden Connection-olio"""

        self._connection=get_database_connection()

    def get_from_history(self):
        """palauttaa kaikkien pelaajien tiedot tietokannasta
        muodossa lista(Tuple(Pelaajan nimi, kerätty määrä rahaa, tila)......)"""

        cursor=self._connection.cursor()
        best_hunters=cursor.execute('SELECT * FROM hunters ORDER BY treasures DESC').fetchall()
        return best_hunters
    def get_three_best_from_history(self):
        """palauttaa kolmen parhaan pelaajan tiedot tietokannasta
        muodossa lista(teksti(Name:'Pelaajan nimi' Treasures:'kerätty määrä' Status: 'Elossa/Koullut')....) 
        """

        cursor=self._connection.cursor()
        best=cursor.execute('SELECT * FROM hunters ORDER BY treasures DESC LIMIT 3').fetchall()
        _return_ = []
        for hunter in best:
            name=hunter[0]
            treasures=str(hunter[1])
            status=hunter[2]
            _return_.append('Name: '+name+' Treasures: '+treasures+' status: '+status)
        return _return_
    def check_name_unique(self, name):
        """Tarkistaa onko nimeja käytetty aikaisemmin
        Args:
            name: uusi nimi, jota halutaan tallentaa tietokantaan
        """

        hunters=self.get_from_history()

        for hunter in hunters:
            if hunter[0]==name:
                return False
        return True

    def write_to_history(self, name, balance, alive):
        """Kirjoittaa pelaajan tiedot tietokantaan
        Args:
            name: pelaajan nimi, jota tallennetaan
            balance: pelaajan kerätyt rahat
            alive: Tieto onko pelaaja pelissä kuollut vai elossa
        """

        c=self._connection.cursor()  # pylint: disable=invalid-name
        c.execute('INSERT INTO hunters(name,treasures,alive) VALUES(?,?,?)',[name,balance, alive])
        self._connection.commit()
    def get_hunter(self, name):
        """Hakee pelaan tiedot tietokannasta nimen perusteella
        palauttaa pelaajan tiedot teksti muodossa:
            'Name: 'Pelaajan nimi' Treasures: 'Kerätyt rahat', Status: 'Elossa/Kuollut' Rank: 'Pelaajan sijoitus taulukossa'
        Jos pelaaja ei löydy tietokannasta palauttaa tekstin 'ei ole tietokannassa'
        Args:
            name: nimi, jonka perusteella etsitään"""
        
        unique_name=self.check_name_unique(name)
        if not unique_name:
            cursor=self._connection.cursor()
            search=cursor.execute('SELECT * FROM(SELECT name,treasures,alive,RANK() OVER (ORDER BY treasures DESC) FROM hunters) WHERE name=?',[name]).fetchone()
            name=search[0]
            treasures=str(search[1])
            status=search[2]
            rank=str(search[3])
            _return_='Name:'+name+'\nTreasures: '+treasures+'\nStatus: '+status+'\n Rank: '+rank
            return _return_
        return 'not such hunter in history'
