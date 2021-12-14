from tkinter import Tk
from ui.ui import UI

def main():
    window=Tk()
    window.geometry('600x400+900+300')

    window.title('Dragon Realm')

    ui=UI(window) # pylint: disable=invalid-name
    ui.start()

    window.mainloop()

if __name__=='__main__':
    main()
