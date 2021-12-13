from tkinter import *
from define.survivetask import SurviveTask

class Surviving1:
    def __init__(self, root, treasure, change, survive_digest):
        self._root=root
        self._treasure=treasure
        self._change=change
        self._open_survive_digest=survive_digest
        self._riddle=None
        self._answer=None
        self._get_task()
        self._frame= None
        self._users=StringVar()
        self._bg=PhotoImage(file='background/survivng.png')

        self._initialize()


    def _get_task(self):
        task=SurviveTask()
        self._riddle=task.riddle()
        self._answer=task.answer()

    def pack(self):
        self._frame.pack(fill=BOTH, side=LEFT, expand=True)

    def destroy(self):
        self._frame.destroy()

    def check(self):
        users=self._users.get()
        if users==self._answer:
            self._open_survive_digest('survive')
        else:
            loss=self._treasure
            self._change(loss)
            self._open_survive_digest('digest', self._answer)
            print('2')

    def _initialize(self):
        self._frame = Frame(master=self._root)

        bg_label=Label(self._frame, image=self._bg)
        bg_label.place(x=0,y=0,relwidth=1, relheight=1)  
        
        info_label = Label(master=self._frame,
            text='To survive answer the riddle with 1 word, use only lowcase letters')

        riddle_label=Label(master=self._frame,
            text=self._riddle)

        self.riddle_answer_entry=Entry(master=self._frame, textvariable=self._users)

        button = Button(
            master=self._frame,
            text="Try to survive")
        button.config(command=self.check)

        info_label.place(relx=.5, rely=0.15, anchor=CENTER)

        riddle_label.place(relx=.5, rely=0.5, anchor=CENTER)

        self.riddle_answer_entry.place(relx=.5, rely=0.85, anchor=CENTER)

        button.place(relx=.5, rely=.95, anchor=CENTER)
