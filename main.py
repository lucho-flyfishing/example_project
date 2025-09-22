# main.py
from tkinter import Tk, StringVar, IntVar
from menus.start_menu import start_menu   # renamed version
from app_state import app_state


def main():
    # Create the single root window
    W = Tk()

    # Set window size and background color
    W.geometry("1200x700")         # <-- adjust size to your design
    W.configure(bg="gray5")       # <-- matches your color scheme

    # Attach Tkinter variables to app_state now that root exists
    app_state.selected_option = IntVar(W)
    app_state.duct_number = IntVar(W)
    app_state.filename = StringVar(W)

    # Start with the start menu
    start_menu(W)

    # Run the Tkinter event loop
    W.mainloop()


if __name__ == "__main__":
    main()