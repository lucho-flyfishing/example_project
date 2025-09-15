from tkinter import Tk
from menus.main_menu import main_menu

W = Tk()
W.title("DUCTS")
W.configure(bg="gray5")
W.geometry('1200x800')

main_menu(W)

W.mainloop()