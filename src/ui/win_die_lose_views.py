from tkinter import messagebox
from define.DefineResult import DefineResult
from tkinter import *
class Result:
    def __init__(self, root, hello, play,treasure, change, survive, write):
        self._root=root
        self._frame=None
        self._open_hello=hello
        self._open_play=play
        self._survive=survive
        self._treasure=treasure
        self._change=change
        self._write=write
        self._status='alive'
        self._background_die=PhotoImage(file='background/inside.png')
        self._bg_loss=PhotoImage(file='background/loss.png')
        self._bg_win=PhotoImage(file='background/gold.png')

        self._determine()

    def _determine(self):
        outcome= DefineResult(self._treasure)
        result=outcome.result()
        if result=='win':
            win=outcome.treasure_change()
            balance=outcome.balance()
            self._change(win)
            self._initialize_win(win, balance)
        elif result=='die':

            self._status='dead'
            self._initialize_die()
        elif result=='lose':
            loss=outcome.treasure_change()
            self._change(loss)
            balance=outcome.balance()
            self._initialize_loss(loss, balance)
        
    def pack(self):
        self._frame.pack(fill=BOTH, side=LEFT, expand=True)

    def destroy(self):
        self._frame.destroy()
    def _last_question(self):
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

    def _info(self):
        infolabel = Label(master=self._frame,
            text="You approach the cave...\nIt is dark and spooky...\nA large dragon jumps out in front of you! He opens his jaws and...")
        infolabel.place(relx=0.5, rely=.1, anchor =CENTER)
    def _initialize_die(self):
        self._frame=Frame(master=self._root)

        background=Label(master=self._frame, image=self._background_die)
        background.place(x=0,y=0,relwidth=1, relheight=1)

        self._info()

        label=Label(master=self._frame, 
        text='Gobbles you down in one bite!')
        survive_button=Button(master=self._frame,
            text='Try to survive?',
            command=self._survive)

        exit_button=Button(master=self._frame,
            text='Go to the afterworld', 
            command=self._last_question)

        label.place(relx=0.5, rely=.5, anchor =CENTER)
        survive_button.place(relx=0.25, rely=.95, anchor =CENTER)
        exit_button.place(relx=0.75, rely=.95, anchor =CENTER)
    
    def _initialize_win(self, win, treasure_balance):
        self._frame=Frame(master=self._root)

        background=Label(master=self._frame, image=self._bg_win)
        background.place(x=0,y=0,relwidth=1, relheight=1)

        self._info()
        result_label=Label(master=self._frame, 
            text='Gives you his treasure!\n+'+str(win))

        treasure_balance_label=Label(master=self._frame, 
            text='Treasures currently:'+str(treasure_balance))

        exit_button=Button(master=self._frame,
            text='Exit the realm \n you will not find road back ever again', 
            command=self._last_question)

        play_button=Button(master=self._frame,
            text='Go Further',
            command=self._open_play)
        result_label.place(relx=.5, rely=.5, anchor =CENTER)
        treasure_balance_label.place(relx=.5, rely=.85, anchor =CENTER)
        play_button.place(relx=.05, rely=.95, anchor =CENTER)
        exit_button.place(relx=.79, rely=.95, anchor =CENTER)


    def _initialize_loss(self, loss, treasure_balance):
        self._frame=Frame(master=self._root)
        background=Label(master=self._frame, image=self._bg_loss)
        background.place(x=0,y=0,relwidth=1, relheight=1)

        self._info()
        result_label=Label(master=self._frame, 
            text='Takes part of your treasures\n -'+str(loss))

        treasure_balance_label=Label(master=self._frame, 
            text='Treasures left: '+str(treasure_balance))

        exit_button=Button(master=self._frame,
            text='Exit the realm \n you will not find road back ever again', 
            command=self._last_question)

        play_button=Button(master=self._frame,
            text='Play again',
            command=self._open_play)

        result_label.place(relx=.5, rely=.5, anchor =CENTER)
        treasure_balance_label.place(relx=.5, rely=.75, anchor =CENTER)
        play_button.place(relx=.25, rely=.95, anchor =CENTER)
        exit_button.place(relx=.75, rely=.95, anchor =CENTER)

