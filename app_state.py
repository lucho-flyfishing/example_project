# app_state.py
# Stores application-wide state variables (no Tkinter root here!)

class AppState:
    def __init__(self):
        self.selected_option = None
        self.duct_number = None
        self.filename = None
        # add more shared variables here later (plain Python types)

# Create one global instance to import everywhere
app_state = AppState()