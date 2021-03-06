from random import choices, randint

class DefineResult:

    """Luokka, joka määrittelee lohikäärmeen tapaamisen tuloksen
    """

    def __init__(self, treasure):
        """Luokan konstruktori
        Args:
            balance: Pelaajan tähän asti kerätyt rahat"""

        self._balance=treasure
        self._treasure_change=None
        self._result=None
        self._determine()

    def _determine(self):

        """Fuoktio kutsuu random tulos funktion ja välittää sen tiedon eteenpäin"""
        
        result=self._randomise_result()
        self._define_result(result)

    def _randomise_result(self):

        """Funktio valitsee tuloksen kolmesta vaihtoehdoisata tietulla todennäköisyydellä
            Returns:
                valitun tuloksen"""

        results=['win', 'die', 'lose']
        probability=[5,1,3]
        result=choices(results,weights=probability)[0]
        return result

    def _define_result(self, result):

        """Funktio määrittelee saamansa tuloksen ja alustaa yhden kolmesta toimeenpiteistä
            Args:
                result: funktion saaama tuolos"""

        if result=='win':
            self._win_result()

        if result=='die':
            self._die_result()

        if result=='lose':
            self._lose_treasure_result()

    def result(self):

        """Returns:
            result: tilanne, jota luokka määritteli pelaajalle seuraavaksi"""

        return self._result

    def treasure_change(self):

        """Returns:
            treasure_change: rahan määrä, jota pelaaja on vaittanut tai hävinnyt luokan määrittelemässä voitto/häviö tilanteessa
            """

        return self._treasure_change

    def balance(self):

        """Returns:
            balance: pelaajan rahatilanne"""

        return self._balance

    def _win_result(self):

        """Funktio asettaa tilanteeksi Voitto-tilanteen, 
            kutsuu funktion, joka määrittää pelaajan voito
            ja asettaa pelaajan uusi rahamäärä"""

        self._result='win'

        self._treasure_change=self._randomise_treasure()

        self._balance+=self._treasure_change

    def _die_result(self):

        """Funktio asettaa tilanteeksi Kuolema'tilanteen"""

        self._result='die'

    def _lose_treasure_result(self):

        """Funktio lähettää saa toiselta funktiolta häviön määrän ja lähettää tarkistavaksi, onko pelaajalla sen verran rahaa ketynyt
            jos rahaa ei ole tarpeeksi:
                lähettää alustavaksi tilanteen Pelaajan kuolema
            jos rahaa on tarpeeksi asettaa:
                treasure change: kuinka paljon on hävinnyt
                balanca: uusi raha-tilanne
                rersult: pelitila: pelaaja on hävinnyt"""

        loss=self._randomise_treasure()
        treasure_balance_check=self._check_treasure_balance(loss)

        if treasure_balance_check:
            self._treasure_change=-loss
            self._balance+=self._treasure_change
            self._result='lose'

        else:
            self._die_result()

    def _randomise_treasure(self):

        """Funktio
            Returns:
                sattunaisen määrän pelirahaa
                """

        return randint(10,1000)

    def _check_treasure_balance(self,loss):

        """Funktio tarkistaa onko pelaajalla tarpeeksi rahaa hävittäväksi
            Args:
                loss: mahdollisen häviön määrä
            Returns:
                True: Pelaajalla on enemmän rahaa tilillä kuin mitä se häviää
                False: Pelaajalla ei ole sen verran rahaa
        """

        if self._balance>loss:
            return True

        return False
