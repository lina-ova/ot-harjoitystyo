from tkinter import StringVar, PhotoImage, constants, Entry, Button, Label, Frame
from define.survivetask import SurviveTask

class Surviving:

    """Luokka, joka alustaa näkymän jossa pelaaja on kuollut ja yrittää pelastua suorittamalla tehtävän
    """

    def __init__(self, root, survive_digest):

        """Luokan konstruktori
        Args:
            root ([tk()]): [tk-olio, vastaa siitä että pelaaja näkee näkymän]
            survive_digest ([funktio]): [kutsuu näkymän, jota näytetään seuraavaksi]
        """

        self._root=root
        self._open_survive_digest=survive_digest
        self._riddle=None
        self._answer=None
        self._get_task()
        self._frame= None
        self._users=StringVar()
        self._bg=PhotoImage(file='src/background/survivng.png')

        self._initialize()

    def _get_task(self):

        """Funktio, joka luo luokan, joka määritää tehtävänannon ja vastauksen
        """

        self.task=SurviveTask()
        self._riddle=self.task.riddle()
        self._answer=self.task.answer()

    def pack(self):

        """Funktio joka kasaa näkymän näytölle"""

        self._frame.pack(fill=constants.BOTH, side=constants.LEFT, expand=True)

    def destroy(self):

        """Funktio, joka tuhoaa näkymän"""

        self._frame.destroy()

    def check(self):

        """Funktio, joka tarkistaa, vastaako pelaajan vastaus oikeaa vai ei ja käskee avaaman seuraa näkymä sen mukaan
        """

        users=self._users.get()
        check=self.task.check_user_answer(self._answer,users)
        self._open_survive_digest(check, self._answer)

    def _initialize(self):

        """Funktio, joka kokoaa kaikki asettaa kaikki näkymä
        """

        self._frame = Frame(master=self._root)

        bg_label=Label(self._frame, image=self._bg)
        bg_label.place(x=0,y=0,relwidth=1, relheight=1)  
        
        info_label = Label(master=self._frame,
            text='To survive answer the riddle with 1 word, use only lowcase letters')

        riddle_label=Label(master=self._frame,
            text=self._riddle)

        self.riddle_answer_entry=Entry(master=self._frame, textvariable=self._users)

        button = Button(
            master=self._frame,
            text="Try to survive")
        button.config(command=self.check)

        info_label.place(relx=.5, rely=0.15, anchor=constants.CENTER)

        riddle_label.place(relx=.5, rely=0.5, anchor=constants.CENTER)

        self.riddle_answer_entry.place(relx=.5, rely=0.85, anchor=constants.CENTER)

        button.place(relx=.5, rely=.95, anchor=constants.CENTER)
