from tkinter import PhotoImage, messagebox, ttk, constants

class SurviveDigestView:
    def __init__(self, root, hello, play, result, answer, write):
        """Luokka, joka vastaa näkymästä, kun pelaaja on kuollut ja yrittänyt pelastua vastaamalla tehtävään

        Args:
            root ([Tk()]): [Tk-olio joka vastaa siitä, että pelaaj avoi nähdä näkymän]
            hello ([funktio]): [käsky, joka avaa pelin alkunäkymän]
            play ([funktio]): [käsky, joka avaa pelin pelaamisenjatkonäkymän]
            result ([text]): [tieto siitä, onko pelaaja pelastunut vai ei]
            answer ([text]): [oikea vastaus tehtävään, jos pelaaja ei pelastunut]
            write ([funktio]): [käsky, joka avaa näkymän, jossa pelaaja voi kirjoittaa nimensa tietokantaan]
        """
        self._root=root
        self._frame=None
        self._open_hello=hello
        self._open_play=play
        self._result=result
        self._answer=answer
        self._write=write
        self._status='dead'
        self._digest_bg=PhotoImage(file='src/background/digest.png')
        self._survive_bg=PhotoImage(file='src/background/survive.png')
        self._define()
    def pack(self):
        """Funktio joka pakkaa kaikki teksti ja napit pelaajalle näytettäväksi
        """
        self._frame.pack(fill=constants.BOTH, side=constants.LEFT, expand=True)

    def destroy(self):
        """Funktio, joka tuhoaa näkymän
        """
        self._frame.destroy()

    def _define(self):
        """Funktio, joka määrittää millaisen tuloksen näyttää pelaajalle, sen perusteella onko se pelastunut vai ei tehtää suorittaessa
        """
        if self._result=='digest':
            self._initialize_digest()
        elif self._result=='survive':
            self._status='alive'
            self._initialize_survived()

    def _last_question(self):
        """Punktio, joka varmistaa pelaajlta, jos se haluaa krijoittaa nimensa tietokantaan pelistä lähtiessä
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

    def _congrats(self):
        """Funktio joka luo näytölle 'Congrats' tekstipätkän
        """
        label=ttk.Label(master=self._frame, text='Congrats!')
        label.place(relx=0.5, rely=0.1, anchor=constants.CENTER)

    def _pooped(self):
        """Funktio, joka luo näytölle 'You were pooped out' tekstipätkän
        """
        label=ttk.Label(master=self._frame, text='You were pooped out')
        label.place(relx=0.5, rely=0.2, anchor=constants.CENTER)

    def _survived(self):
        """Funktio, joka luo näytölle 'You survived and still got your treasures' tekstipätkän
        """
        label=ttk.Label(master=self._frame, text='You survived and still got your treasures')
        label.place(relx=0.5, rely=0.45, anchor=constants.CENTER)

    def _worth_it(self):
        """Funktio, joka luo näytölle 'But was it all worth it?' tekstipätkän
        """
        label=ttk.Label(master=self._frame, text='But was it all worth it?')
        label.place(relx=0.5, rely=0.55, anchor=constants.CENTER)
    def _initialize_survived(self):
        """Funktio joka luo näkymän tilanteessa, jossa pelaaja on pelastunut"""
        self._frame=ttk.Frame(master=self._root)
        background=ttk.Label(master=self._frame, image=self._survive_bg)
        background.place(x=0,y=0,relwidth=1, relheight=1)
        self._congrats()
        self._pooped()
        self._survived()
        self._worth_it()
        play_button=ttk.Button(
            master=self._frame, 
            text='Go further',
            command=self._open_play
        )
        exit_button=ttk.Button(
            master=self._frame,
            text='Exit the realm forever and go to shower',
            command=self._last_question
        )
        play_button.place(relx=0.25, rely=0.95, anchor=constants.CENTER)
        exit_button.place(relx=0.75, rely=0.95, anchor=constants.CENTER)
    def _correct_answer(self):
        """Funktio joka asettaa näytölle 'Correct aswer was' ja oikean vastauksen
        """
        label_info=ttk.Label(master=self._frame, text='Correct answer was:')
        label_answer=ttk.Label(master=self._frame, text=self._answer)

        label_info.place(relx=0.5, rely=0.1, anchor=constants.CENTER)
        label_answer.place(relx=0.5, rely=0.2, anchor=constants.CENTER)
    def _unfortune(self):
        """Funktio joka asettaa näytölle 'Unfortunately you could not survive and got digested'
        """
        label=ttk.Label(master=self._frame, text='Unfortunately you could not survive and got digested')
        label.place(relx=0.5, rely=0.45, anchor=constants.CENTER)
    def _initialize_digest(self):
        """Funktio,joka luo näytölle näkymän tilanteessa, kun pelaaja ei pelastunut
        """
        self._frame=ttk.Frame(master=self._root)

        background=ttk.Label(master=self._frame, image=self._digest_bg)
        background.place(x=0,y=0,relwidth=1, relheight=1)

        self._correct_answer()
        self._unfortune()
        self._worth_it()
        exit_button=ttk.Button(
            master=self._frame,
            text='go to the afterworld',
            command=self._last_question
        )
        exit_button.place(relx=0.5, rely=0.95, anchor=constants.CENTER)