from tkinter import messagebox, PhotoImage, Label, Frame, Button, BOTH, LEFT, CENTER
from define.define_result import DefineResult
class Result:
    def __init__(self, root, hello, play,treasure, change, survive, write):
        """Luokka, joka vastaa pelaajan valinnan jälkeisestä näkymästä, pelaaja joko kuolee, voittaa tai häviää rahaa

        Args:
            root ([tk]): [tk-oli, pelinnäyttö]
            hello ([funktio]): [käsky, joka avaa pelin alkunäkymän]
            play ([funktio]): [käsky, joka avaa pelin pelinäkymän]
            treasure ([int]): [pelaajan rahamäärä]
            change ([funktio]): [käsky, joka vaihtaa pelaajan rahaatilannetta, jos hän häviää tai voittaa]
            survive ([funktio]): [tilanteessa jossa pelaaja on kuollut ja haluaa yrittää pelastua, avaa näkymän jossa pelaaja saa tehtävän suoritettavaksi]
            write ([funktio]): [käsky, joka avaa näkymän, jossa pelaaja voi kirjoittaa tietojaan tietokantaan]
        """
        self._root=root
        self._frame=None
        self._open_hello=hello
        self._open_play=play
        self._survive=survive
        self._treasure=treasure
        self._change=change
        self._write=write
        self._status='alive'
        self._background_die=PhotoImage(file='src/background/inside.png')
        self._bg_loss=PhotoImage(file='src/background/loss.png')
        self._bg_win=PhotoImage(file='src/background/gold.png')

        self._determine()

    def _determine(self):
        """Funktio, joka luo luoka, joka määrittelee teidon siitä, onko pelaaja kuollut/pelastunut/ hävinnyt
            suorittaa toimenpiteitä sen mukaan, mikä tulos on
        """
        outcome= DefineResult(self._treasure)
        result=outcome.result()
        if result=='win':
            win=outcome.treasure_change()
            balance=outcome.balance()
            self._change(win)
            self._initialize_win(win, balance)
        elif result=='die':

            self._status='dead'
            self._initialize_die()
        elif result=='lose':
            loss=outcome.treasure_change()
            self._change(loss)
            balance=outcome.balance()
            self._initialize_loss(loss, balance)
        
    def pack(self):
        """Funktio, joka pakkaa näkymän, näytölle
        """
        self._frame.pack(fill=BOTH, side=LEFT, expand=True)

    def destroy(self):
        """Funktio, joka tuhoaa näkymän, ennen seuraavan näkymän alustusta
        """
        self._frame.destroy()
    def _last_question(self):
        """Funktio, joka tilanteessa, jossa pelaaja haluaa sulkea pelin, kysyy, jos pelaaja haluaa kirjoittaa tietojaan tietokantaan
        """
        question=messagebox.askyesno('book of hunters', 'Do you want to write yor name in history?')
        if question:
            self._write(self._status)
        else:
            if self._status=='alive':
                message='Enjoy your life and treasures'
            else:
                message='Enjoy your afterlife'
            info=messagebox.showinfo('', message)
            if info:
                self._root.destroy()

    def _info(self):
        """Funktio, joka luo näkymään alkutekstin, joka on sama tuloksesta riippumatta
        """
        infolabel = Label(master=self._frame,
            text="You approach the cave...\nIt is dark and spooky...\nA large dragon jumps out in front of you! He opens his jaws and...")
        infolabel.place(relx=0.5, rely=.1, anchor =CENTER)
    def _initialize_die(self):
        """Funktio, joka alustaa teksti ja napin, tuloksessa, jossa pelaaja on kuollut
        """
        self._frame=Frame(master=self._root)

        background=Label(master=self._frame, image=self._background_die)
        background.place(x=0,y=0,relwidth=1, relheight=1)

        self._info()

        label=Label(master=self._frame, 
        text='Gobbles you down in one bite!')
        survive_button=Button(master=self._frame,
            text='Try to survive?',
            command=self._survive)

        exit_button=Button(master=self._frame,
            text='Go to the afterworld', 
            command=self._last_question)

        label.place(relx=0.5, rely=.5, anchor =CENTER)
        survive_button.place(relx=0.25, rely=.95, anchor =CENTER)
        exit_button.place(relx=0.75, rely=.95, anchor =CENTER)
    
    def _initialize_win(self, win, treasure_balance):
        """Funktio, joka alustaa näkymän tilanteessa, jossa pelaaja on voittanut

        Args:
            win ([int]): [pelaajn voittomäärä]
            treasure_balance ([int]): [pelaajan uusi rahatilanne]
        """
        self._frame=Frame(master=self._root)

        background=Label(master=self._frame, image=self._bg_win)
        background.place(x=0,y=0,relwidth=1, relheight=1)

        self._info()
        result_label=Label(master=self._frame, 
            text='Gives you his treasure!\n+'+str(win))

        treasure_balance_label=Label(master=self._frame, 
            text='Treasures currently:'+str(treasure_balance))

        exit_button=Button(master=self._frame,
            text='Exit the realm \n you will not find road back ever again', 
            command=self._last_question)

        play_button=Button(master=self._frame,
            text='Go Further',
            command=self._open_play)
        result_label.place(relx=.5, rely=.5, anchor =CENTER)
        treasure_balance_label.place(relx=.5, rely=.85, anchor =CENTER)
        play_button.place(relx=.05, rely=.95, anchor =CENTER)
        exit_button.place(relx=.79, rely=.95, anchor =CENTER)


    def _initialize_loss(self, loss, treasure_balance):
        """FUnktio, joka alustaa näkymän, tilanteessa, jossa pelaaja on hävinnyt osan rahasta

        Args:
            loss ([int]): [häviön määrä]
            treasure_balance ([int]): [pelaajan uusi tämänhetkinen rahatilanne]
        """
        self._frame=Frame(master=self._root)
        background=Label(master=self._frame, image=self._bg_loss)
        background.place(x=0,y=0,relwidth=1, relheight=1)

        self._info()
        result_label=Label(master=self._frame, 
            text='Takes part of your treasures\n -'+str(loss))

        treasure_balance_label=Label(master=self._frame, 
            text='Treasures left: '+str(treasure_balance))

        exit_button=Button(master=self._frame,
            text='Exit the realm \n you will not find road back ever again', 
            command=self._last_question)

        play_button=Button(master=self._frame,
            text='Go Further',
            command=self._open_play)

        result_label.place(relx=.5, rely=.5, anchor =CENTER)
        treasure_balance_label.place(relx=.5, rely=.75, anchor =CENTER)
        play_button.place(relx=.25, rely=.95, anchor =CENTER)
        exit_button.place(relx=.75, rely=.95, anchor =CENTER)

