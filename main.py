from tkinter import Tk
from menus.main_menu import main_menu

W = Tk()
W.title("DUCTS")
W.configure(bg="gray12")

main_menu(W)

W.mainloop()