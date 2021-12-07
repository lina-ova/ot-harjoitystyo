from tkinter import *

class MakeChoiceView:
    def __init__(self, root,define_result, treasure):
        self._root = root
        self._frame = None
        self._define_result=define_result
        self._treasure=treasure
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
            command=self._define_result)
        treasure_label=Label(master=self._frame,
        text='Treasures currently: '+str(self._treasure))
        label.grid(padx=10, pady=10)
        treasure_label.grid(padx=10,pady=10)
        button.grid(padx=10,pady=10)