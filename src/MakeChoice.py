from tkinter import *

import time

class MakeChoiceView:
    def __init__(self, root,show_result):
        self._root = root
        self._frame = None
        self._handle_show_result=show_result
        self._initialize()

    def pack(self):
        self._frame.pack(fill=X)

    def destroy(self):
        self._frame.destroy()
            

    def _initialize(self):
        self._frame = Frame(master=self._root)
        label = Label(master=self._frame,
            text="You approach the cave...\nIt is dark and spooky...\nA large dragon jumps out in front of you! He opens his jaws and...")
        button = Button(master=self._frame,
            text='Show the result',
            command=self._handle_show_result)
        label.grid(padx=10, pady=10)
        button.grid(padx=10,pady=10)