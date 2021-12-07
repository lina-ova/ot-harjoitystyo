

from tkinter import *
from HelloView import HelloView
from play import PlayView
from Win import WinView
from Die import DieView
from Loss import LossView
from database_connection import get_database_connection
from MakeChoice import MakeChoiceView
from DefineView import Result
from Survive_task import SurviveTask
from Surviving import Surviving
from cheking_answers import Cheking


class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._treasure = 0

    def start(self):
        self._show_hello_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _change_treasure_value(self, value):
        self._treasure+=value

    def _handle_play(self):
        self._show_play_view()   

    def _handle_hello(self):
        self._show_hello_view()

    def _handle_choice_made(self):
        self._show_choice_made_view()

    def _handle_win(self, win):
        self._show_win_view(win)
    
    def _handle_die(self):
        self._show_die_view()
    
    def _handle_lose(self, loss):
        self._show_lose_view(loss)

    def _handle_survive(self):
        self._survive_task_generation()
    
    def _handle_surviving(self, riddle, answer):
        self._show_surviving_view(riddle, answer)


    def _show_hello_view(self):
        self._hide_current_view()

        self._current_view = HelloView(
            self._root,
            self._handle_play,
            self._treasure
        )

        self._current_view.pack()

    def _show_play_view(self):
        self._hide_current_view()

        self._current_view = PlayView(
            self._root,
            self._handle_hello,
            self._handle_choice_made, 
            self._treasure
        )

        self._current_view.pack()
    
    def _show_choice_made_view(self):
        self._hide_current_view()
        self._current_view=MakeChoiceView(
            self._root,
            self._define_result,
            self._treasure
        )

        self._current_view.pack()
        
    def _define_result(self):
        define_result=Result(
            self._treasure,
            self._change_treasure_value, 
            self._handle_win,
            self._handle_die,
            self._handle_lose
        )

    def _show_lose_view(self, loss):
        self._hide_current_view()
        self._current_view=LossView(
            self._root,
            self._handle_hello,
            self._handle_play,
            self._treasure, 
            loss
        )
        self._current_view.pack()   
    def _show_win_view(self, win):
        self._hide_current_view()
        self._current_view=WinView(
            self._root,
            self._handle_hello,
            self._handle_play, 
            self._treasure,
            win 
        )
        self._current_view.pack()
    def _show_die_view(self):
        self._hide_current_view()
        self._current_view=DieView(
            self._root,
            self._handle_hello, 
            self._handle_survive 
        )
        self._current_view.pack()
    
    def _show_surviving_view(self, riddle, answer):
        self._hide_current_view()
        self._current_view=Surviving(
            self._root,
            riddle,
            answer,
            self._handle_play,
            self._handle_hello
        )
        self._current_view.pack()
    
    def _survive_task_generation(self):
        survive=SurviveTask(get_database_connection(),
            self._handle_surviving
       )
    def _check_answers(self, correct, users):
        check=Cheking(correct, users, self._handle_hello, self._handle_play)



    

window = Tk()
window.title("Dragon realm")

ui = UI(window)
ui.start() 

window.mainloop()