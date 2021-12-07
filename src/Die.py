from tkinter import *

class DieView:
    def __init__(self, root, handle_hello, handle_survive):
        self._root=root
        self._frame=None
        self._handle_hello=handle_hello
        self._survive=handle_survive
        self._initialize()

    def pack(self):
        self._frame.pack(fill=X)
    
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame=Frame(master=self._frame)
        label=Label(master=self._frame, 
        text='Gobbles you down in one bite!')
        survive_button=Button(master=self._frame,
            text='Try to survive?',
            command=self._survive)
        exit_button=Button(master=self._frame,
            text='Exit', 
            command=self._handle_hello)

        label.grid(row=1, padx=10, pady=10)
        survive_button.grid(row=2, padx=10, pady=10)
        exit_button.grid(row=3, padx=10, pady=10)