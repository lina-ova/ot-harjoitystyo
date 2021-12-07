from tkinter import *

class LossView:
    def __init__(self, root, handle_hello, handle_play, treasure, loss):
        self._root=root
        self._frame=None
        self._handle_hello=handle_hello
        self._handle_play=handle_play
        self._treasure=treasure
        self._loss=loss
        self._initialize()

    def pack(self):
        self._frame.pack(fill=X)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame=Frame(master=self._frame)
        result_label=Label(master=self._frame, 
            text='Takes part of your treasures\n -'+str(self._loss))
        treasure_balance_label=Label(master=self._frame, 
            text='Treasures left: '+str(self._treasure))
        exit_button=Button(master=self._frame,
            text='Exit the realm', 
            command=self._handle_hello)

        play_button=Button(master=self._frame,
            text='Play again',
            command=self._handle_play)

        result_label.grid(row=1, column=2, padx=10, pady=10)
        treasure_balance_label.grid(row=2, column=2, padx=10, pady=10)
        play_button.grid(row=2, column=1, padx=10, pady=10)
        exit_button.grid(row=2, column=3, padx=10, pady=10)