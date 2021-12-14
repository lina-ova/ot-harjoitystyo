from tkinter import constants
from tkinter import *


class PlayView:
    def __init__(self, root, make_choice, treasure):
        """Luokka, joka vastaa pelinäkymästä, jossa pelaaja valitsee kahden luolan välissä

        Args:
            root ([tk]): [tk-olio, pelinnäyttö]
            make_choice ([funktio]): [käsky, joka avaa seuraavan näkymän]
            treasure ([int]): [tieto, minkä verran pelaaja on kerännyt rahaa]
        """
        self._root = root
        self._frame = None
        self._make_choice= make_choice
        self._treasure=treasure
        self._bg=PhotoImage(file='src/background/play_view.png')
        self._initialize()

    def pack(self):
        """Funktio, joka pakaa näkymä näytölle
        """
        self._frame.pack(fill=constants.BOTH, side=constants.LEFT, expand=True)

    def destroy(self):
        """Funktio, joka tuhoaa näkymän, ennen seuravan näkymän alustamista"""
        self._frame.destroy()
  
    def _initialize(self):
        """Funktio, joka alustaa näkymän"""
        
        self._frame = Frame(master=self._root)

        bg_label=Label(self._frame, image=self._bg)
        bg_label.place(x=0,y=0,relwidth=1, relheight=1)

        text_label=Label(
            master=self._frame, 
            text='You are in a land full of dragons. In front of you,\nyou see two caves. In one cave, the dragon is friendly\nand will share his treasure with you. The other dragon\nis greedy and hungry, and will eat you on sight.\nWhich cave will you go into?',
            background='#1E90FF')
        

        cage1_button=Button(
            master=self._frame,
            text='Cage 1',
            command=self._make_choice
        )
        cage2_button=Button(
            master=self._frame,
            text='Cage 2',
            command=self._make_choice,
        )
        treasure_label=Label(master=self._frame, 
        text='Treasures currently: '+str(self._treasure), background='#1E90FF')

        text_label.place(relx=.5, rely=.15, anchor=CENTER)
        cage1_button.place(relx=.25, rely=.55, anchor=CENTER)
        cage2_button.place(relx=.75, rely=.55, anchor=CENTER)
        treasure_label.place(relx=.75, rely=.95, anchor=CENTER)
        