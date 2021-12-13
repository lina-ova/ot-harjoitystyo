from tkinter import *
from ui.HelloView import HelloView
from ui.play import PlayView
from ui.surviving1 import Surviving1
from ui.win_die_lose_views import Result
from ui.Digest_survive import SurviveDigestView
from ui.hunters_in_history import HistoryView
from ui.Write_in_HIstory import WriteView
class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._treasure = 0
        self._status='alive'


    def start(self):
        self._show_hello_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
    def _change_status(self):
        self._status='dead'
    def _change_treasure_value(self, value):
        self._treasure+=value

    def _show_hello_view(self):
        self._hide_current_view()

        self._current_view = HelloView(
            self._root,
            self._show_play_view,
            self._show_history_view
        )
        self._current_view.pack()



    def _show_play_view(self):
        self._hide_current_view()

        self._current_view = PlayView(
            self._root,
            self._result,
            self._treasure
        )
        self._current_view.pack()
    
    def _result(self):
        self._hide_current_view()

        self._current_view=Result(
            self._root,
            self._show_hello_view,
            self._show_play_view,
            self._treasure,
            self._change_treasure_value,
            self._surviving,
            self._show_write_view

        )
        self._current_view.pack()    

    def _show_write_view(self, status):
        self._hide_current_view()
        self._current_view=WriteView(
            self._root,
            self._treasure,
            status
        )
        self._current_view.pack()
    def _surviving(self):
        self._hide_current_view()
        self._current_view=Surviving1(
            self._root,
            self._treasure,
            self._change_treasure_value,
            self._show_digest_survive 
        )
        self._current_view.pack()

    def _show_digest_survive(self,result, answer=None):
        self._hide_current_view()
        self._current_view=SurviveDigestView(
            self._root,
            self._show_hello_view,
            self._show_play_view,
            result,
            answer,
            self._show_write_view
        )
        self._current_view.pack()

    def _show_history_view(self):
        self._hide_current_view()
        self._current_view=HistoryView(
            self._root, 
            self._show_hello_view)
        self._current_view.pack()