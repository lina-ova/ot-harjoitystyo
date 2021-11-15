from tkinter import *

class PlayView:
    def __init__(self, root, handle_hello, make_choice):
        self._root = root
        self._handle_hello = handle_hello
        self._frame = None
        self._make_choice= make_choice

        self._initialize()

    def pack(self):
        self._frame.pack(fill=X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = Frame(master=self._root)
        text_label=Label(
            master=self._frame, 
            text='You are in a land full of dragons. In front of you,\nyou see two caves. In one cave, the dragon is friendly\nand will share his treasure with you. The other dragon\nis greedy and hungry, and will eat you on sight.\nWhich cave will you go into?',
            font=('Helvetica', 24))
    
        cage1_button=Button(
            master=self._frame,
            text='Cage 1',
            command=self._make_choice
        )
        cage2_button=Button(
            master=self._frame,
            text='Cage 2',
            command=self._make_choice
        )
        button = Button(
            master=self._frame,
            text="Pause the game",
            command=self._handle_hello
        )
        text_label.grid(row=0,column=1,padx=10, pady=10)
        cage1_button.grid(row=1, column=0,padx=50, pady=50)
        cage2_button.grid(row=1, column=2,padx=50,pady=50)
        button.grid(row=2, column=1, padx=10, pady=10)




    