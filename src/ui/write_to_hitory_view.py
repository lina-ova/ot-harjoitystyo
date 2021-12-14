
from tkinter import *
from tkinter import messagebox
from define.best_hunters import Hunters
class WriteView:
    def __init__(self, root, treasure,status):
        """Luokka, joka vastaa näkymästä, jossa pelaaja haluaa ennen pelistä lähtöäkirjoittaa tietojaan tietokantaan

        Args:
            root ([tk]): [tk-oli, pelinäytttö]
            treasure (int): [pelaajan rahatilanne]
            status ([text]): [tieto siitä onko pelaaja kuollut vai elossa]
        """
        self._root=root
        self._treasure=treasure
        self._status=status
        self._name=StringVar()
        self._bg=PhotoImage(file='src/background/book.png')
        self._init()
    def pack(self):
        """Funktio, joka pakkaa näkymän näytölle
        """
        self._frame.pack(fill=BOTH, side=LEFT, expand=True)

    def _init(self):
        """FUnktio, joka alustaa näkymälle kaikki tiedot, tekstikenttä ja napit
        """
        self._frame=Frame(master=self._root)
        bg_label=Label(self._frame, image=self._bg)
        bg_label.place(x=0,y=0,relwidth=1, relheight=1)  
        
        treasures=Label(
            master=self._frame,
            text='Treasures: '+str(self._treasure)
        )
        status=Label(
            master=self._frame,
            text='Status: '+self._status
        )
        name=Label(
            master=self._frame,
            text='How do you want people to remember you?'
        )
        name_entry=Entry(
            master=self._frame, textvariable=self._name)
        remember=Button(master=self._frame,text='Write the name',command=self._check)
        not_remember=Button(master=self._frame,text='Stay unkown', command=self._stay_unknown)

        treasures.place(relx=.25, rely=.25, anchor=CENTER)
        status.place(relx=.75, rely=.25, anchor=CENTER)
        name.place(relx=.25, rely=.5, anchor=CENTER)
        name_entry.place(relx=.75, rely=.5, anchor=CENTER)
        remember.place(relx=.25, rely=.75, anchor=CENTER)
        not_remember.place(relx=.75, rely=.75, anchor=CENTER)
        
    def _stay_unknown(self):
        """FUnktio, joka kutsuu viestin pelaajalle näytettäväksi tilanteessa, jossa pelaaja päättää jäättä tietojaan tallentamatta
        """
        if self._status=='alive':
            message='             Fine!\n Stay unknown and rich'
        else:
            message='             Fine!\n Stay unknown and dead'
        info=messagebox.showinfo('Stay unknown', message)
        if info:
            self._root.destroy()

    def _check(self):
        """Funktio, joka tarkistaa, onko nimi, jota pelaaja haluaa tallentaa tietokantaan varattu vai ei.
            Funktio ei hyväksy tyhjää merkkijonoa. 
            Jos nimi ei ole varattu, eikä tyhjä, varmistaa pelaajalta, että hän haluaa kirjoittaa sen
        """
        hunters=Hunters()
        name=self._name.get()

        check=hunters.check_name_unique(name)
        if check and len(name)>0:
            message='Are you sure you want to be remembered as '+name+'?'
            remember=messagebox.askyesno('To remember?', message)
            if remember:
                hunters.write_to_history(name, self._treasure, self._status)
                message='History will remember you '+name
                m=messagebox.showinfo('Book', message)
                if m:
                    self._root.destroy()
        else:
            messagebox.showinfo('Book', 'History already knows treasure hunter with this name')
    

    
