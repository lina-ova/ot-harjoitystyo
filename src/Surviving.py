from tkinter import *

class Surviving:
    def __init__(self, root,  riddle, answer, check):
        self._root=root
        self._frame= None
        self._riddle=riddle
        self._answer=answer
        self._handle_check=check
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(master=self._root)
        info_label = Label(master=self._frame,
            text='To survive answer the riddle with 1 word, use only lowcase letters')

        riddle_label=Label(master=self._frame,
            text=self._riddle)

        self._riddle_answer_entry=Entry(master=self._frame)

        button = Button(
            master=self._frame,
            text="Try to survive",
            command=self._handle_check(self._riddle_answer_entry.get(), self._answer)
        )

        info_label.grid(row=1,padx=10, pady=10)

        riddle_label.grid(row=2,padx=10, pady=10)

        self._riddle_answer_entry.grid(row=3,padx=10, pady=10)

        button.grid(row=4,padx=10, pady=10)



        