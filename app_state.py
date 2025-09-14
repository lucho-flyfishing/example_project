from tkinter import Tk

class AppState:
    def __init__(self):
        self.selected_option = None
        self.duct_number = None
        # add more shared vars here

# Create global state and window
app_state = AppState()
W = Tk()