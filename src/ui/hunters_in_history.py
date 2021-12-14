from tkinter import Frame, Label, Entry, Button, PhotoImage, messagebox, StringVar
from tkinter.constants import BOTH, CENTER, LEFT
from define.best_hunters import Hunters
class HistoryView:
    def __init__(self, root, hello):
        """Luokka, joka vastaa History-näkymästä, jossa on entiset pelaajat ja niiden tietojen hakeminen tietokannasta

        Args:
            root ([tk]): [pelinnäyttö]
            hello ([funktio]): [käsky, joka avaa pelin alunäkymän]
        """
        self._root=root
        self._frame=None
        self._open_hello=hello
        self._hunters=Hunters()
        self._search_name=StringVar()
        self._background=PhotoImage(file='src/background/book.png')

        self._initialize()
    def destroy(self):
        """funktio, tuhoaa, näkymän, ennen seuraava näyttämistä
        """
        self._frame.destroy()

    def pack(self):
        """funktio, joka pakkaa näkymän näytölle
        """
        self._frame.pack(fill=BOTH, side=LEFT, expand=True)

    def _initialize(self):
        """Funktio, joka asettaa kaikki tiedot näkymälle"""
        self._frame=Frame(master=self._root)

        background=Label(master=self._frame, image=self._background)

        background.place(x=0,y=0,relwidth=1, relheight=1)

        self._initialize_hunters()

        search_entry=Entry(self._frame, textvariable=self._search_name)
        
        search_button=Button(
            master=self._frame, 
            text='Search for hunter in history',
            command=self._search)

        close_button=Button(
            master=self._frame,
            text='close the book of hunters',
            command=self._open_hello
        )

        
        search_entry.place(relx=0.5, rely=0.5, anchor=CENTER)
        search_button.place(relx=0.5, rely=0.75, anchor=CENTER)
        close_button.place(relx=0.5, rely=0.95, anchor=CENTER)

    def _initialize_hunters(self):
        """Funktio, joka asettaa näkymälle kolme parasta pelaajaa
        """
        three_best_hunters=self._hunters.get_three_best_from_history()

        best=Label(master=self._frame, text=three_best_hunters[0])
        second=Label(master=self._frame, text=three_best_hunters[1])
        third=Label(master=self._frame, text=three_best_hunters[2])

        best.place(relx=0.5, rely=0.1, anchor=CENTER)
        second.place(relx=0.5, rely=0.2, anchor=CENTER)
        third.place(relx=0.5, rely=0.3, anchor=CENTER)

    def _search(self):
        """Funktio, joka lukee pelaajan syöteen ja etsi sen perusteella tietokannasta tietoa 
        """
        name=self._search_name.get()
        search_result=self._hunters.get_hunter(name)
        messagebox.showinfo('Book', search_result)
        


        

