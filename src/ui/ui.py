from tkinter import *
from ui.hello_view import HelloView
from ui.play import PlayView
from ui.surviving_view import Surviving
from ui.win_die_lose_views import Result
from ui.digest_survive import SurviveDigestView
from ui.hunters_in_history import HistoryView
from ui.write_to_hitory_view import WriteView
class UI:
    """Luokka, joka vastaa näkyminen välisestä siirtymisestä
    """
    def __init__(self, root):
        """Luokka-konstruktori

        Args:
            root ([tk]): [tk-olio, pelinnäyttö]
        """
        self._root = root
        self._current_view = None
        self._treasure = 0

    def start(self):
        """Funktio, joka, avaa pelinalkunäkymän
        """
        self._show_hello_view()

    def _hide_current_view(self):
        """Funktio, joka tuhoaa näkymän
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _change_treasure_value(self, value):
        """Funktio, joka vaihtaa pelajanrahatilanteen

        Args:
            value ([int]): [määrä, jolla rahatilanne on vaihtunut]
        """
        self._treasure+=value

    def _show_hello_view(self):
        """Funtio, joka tuhoaa edellisen näkymän, alustaa alkunäkymän ja pakkaa sen näytölle
        """
        self._hide_current_view()

        self._current_view = HelloView(
            self._root,
            self._show_play_view,
            self._show_history_view
        )
        self._current_view.pack()



    def _show_play_view(self):
        """Funtio, joka tuhoaa edellisen näkymän, alustaa pelinäkymän ja pakkaa sen näytölle
        """
        self._hide_current_view()

        self._current_view = PlayView(
            self._root,
            self._result,
            self._treasure
        )
        self._current_view.pack()
    
    def _result(self):
        """Funtio, joka tuhoaa edellisen näkymän, alustaa pelitulosnäkymän ja pakkaa sen näytölle
        """
        self._hide_current_view()

        self._current_view=Result(
            self._root,
            self._show_hello_view,
            self._show_play_view,
            self._treasure,
            self._change_treasure_value,
            self._surviving,
            self._show_write_view

        )
        self._current_view.pack()    

    def _show_write_view(self, status):
        """Funtio, joka tuhoaa edellisen näkymän, alustaa näkymän, jossa pelaaja kirjoittaa tietojaan tietokantaan ja pakkaa sen näytölle

        Args:
            status ([text]): [teito siitä, onko pelaaja elossa vai kuollut]
        """
        self._hide_current_view()
        self._current_view=WriteView(
            self._root,
            self._treasure,
            status
        )
        self._current_view.pack()
    def _surviving(self):
        """Funtio, joka tuhoaa edellisen näkymän, alustaa näkymän, jossa pelaaja yrittää suoritta tehtävän pelastuakseen ja pakkaa sen näytölle
        """
        self._hide_current_view()
        self._current_view=Surviving(
            self._root,
            self._show_digest_survive 
        )
        self._current_view.pack()

    def _show_digest_survive(self,result, answer=None):
        """Funtio, joka tuhoaa edellisen näkymän, alustaa näkymän, jossa pelaaja tehtävän suorittaessa pelastunut tai kuollut ja pakkaa sen näytölle

        Args:
            result ([text]): [tieto siitä, onko pelaaja koullut vai elossa]
            answer ([text], optional): [oikea vastaus tehtävään, välietetään, jos pelaaja ei pelastunut]. Defaults to None.
        """
        self._hide_current_view()
        self._current_view=SurviveDigestView(
            self._root,
            self._show_hello_view,
            self._show_play_view,
            result,
            answer,
            self._show_write_view
        )
        self._current_view.pack()

    def _show_history_view(self):
        """Funtio, joka tuhoaa edellisen näkymän, alustaa näkymän, jossa pelaaja voi kattoa edellisten pelaajien suorituksia tietokannasta ja pakkaa sen näytölle
        """
        self._hide_current_view()
        self._current_view=HistoryView(
            self._root, 
            self._show_hello_view)
        self._current_view.pack()