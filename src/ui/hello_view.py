from tkinter import    Label, PhotoImage, ttk, constants

class HelloView:
    def __init__(self, root, handle_play, history):
        """Luokka, joka vastaa pelin alkunäkymästä

        Args:
            root ([tk()]): [tk-olio, pelin näyttö]
            handle_play ([funktio]): [käsky, joka avaa pelinnäkymän]
            history ([funktio]): [käsky, joka avaa parhaat pelaaajat teulukon ja näkymän]
        """
        self._root = root
        self._handle_play = handle_play
        self._show_history=history
        self._frame = None
        self._bg=PhotoImage(file='src/background/hello.png')
        

        self._initialize()

    def pack(self):
        """Funktio pakkaa kaikki näytölle
        """
        self._frame.pack(fill=constants.BOTH, side=constants.LEFT, expand=True)

    def destroy(self):
        """Funktio, joka tuhoaa näkymän
        """
        self._frame.destroy()

    
        
    def _initialize(self):
        """Funktio, joka asettaa näkymälle tekstit ja napit 
        """
        style=ttk.Style()
        style.configure('Style.TButton', background='#1E90FF')

        self._frame = ttk.Frame(master=self._root)
        bg_label=Label(self._frame, image=self._bg)
        bg_label.place(x=0,y=0,relwidth=1, relheight=1)
        self.pack()

        
        label = ttk.Label(self._frame,
            text="Hello Travaller!", background='#1E90FF')
        
        enter_button = ttk.Button(
            master=self._frame,
            text="Enter The Dragon Realm", style='Style.TButton',
            command=self._handle_play
        )
        history_button=ttk.Button(
            master=self._frame,
            text='Show History of Treasure Hunters', style='Style.TButton',
            command=self._show_history
        )

        label.place(relx=0.5, rely=0.15, anchor=constants.CENTER)
        enter_button.place(relx=0.5, rely=0.5, anchor=constants.CENTER)
        history_button.place(relx=0.5, rely=0.95, anchor=constants.CENTER)

