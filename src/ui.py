from tkinter import *
from HelloView import HelloView
from play import PlayView
from MakeChoice import MakeChoiceView
from ResultView import ResultView

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

    def _handle_play(self):
        self._show_play_view()   

    def _handle_hello(self):
        self._show_hello_view()

    def _handle_choice_made(self):
        self._show_choice_made_view()

    def _handle_result(self):
        self._show_result_view()


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
            self._show_result_view,
            self._treasure
        )

        self._current_view.pack()
        
    def _show_result_view(self):
        self._hide_current_view()
        self._current_view=ResultView(
            self._root,
            self._handle_hello, 
            self._treasure
        )
        self._current_view.pack()
    


    

window = Tk()
window.title("Dragon realm")

ui = UI(window)
ui.start()

window.mainloop()