class Cheking:
    def __init__(self, correct, users, hello, play ):
        self._correct=correct
        self._users=users
        self._hello=hello
        self._play=play
        self._define()
    
    def _define(self):
        if self._correct==self._users:
            self._play
        else:
            self._hello