from tkinter import *
import random
class ResultView:
    def __init__(self, root, handle_hello, treasure):
        self._root = root
        self._frame = None
        self._handle_hello=handle_hello
        self._treasure=treasure
        self._initialize()

    def pack(self):
        self._frame.pack(fill=X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        result=random.randint(1,2)
        if result==1:
            treasure=random.randint(10,1000)
            self._treasure+=treasure
            text='Gives you his treasure!\n'+str(treasure)+'!'

        elif result==2:
            text='Gobbles you down in one bite!'
        self._frame = Frame(master=self._root)
        label = Label(master=self._frame,
            text=text)
        treasure_label=Label(master=self._frame,
            text='Treasure currently:'+str(self._treasure))
        
        button = Button(
            master=self._frame,
            text="Exit the realm",
            command=self._handle_hello
        )
        label.grid(row=0,column=1,padx=10, pady=10)
        treasure_label.grid(row=1)
        button.grid(row=2, column=1, padx=10, pady=10)