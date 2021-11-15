from tkinter import ttk, constants

class HelloView:
    def __init__(self, root, handle_play):
        self._root = root
        self._handle_play = handle_play
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame,
            text="Hello!")
        
        button = ttk.Button(
            master=self._frame,
            text="Enter Dragon Realm",
            command=self._handle_play
        )

        label.grid(padx=10, pady=10)
        button.grid(padx=10, pady=10)

