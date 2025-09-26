# app_state.py
# Stores application-wide state variables (no Tkinter root here!)

class AppState:
    def __init__(self):
        self.filename = None
        self.duct_number = None
        self.main_branch = None
        self.selected_option = None
        # add more shared variables here later (plain Python types)

# Create one global instance to import everywhere
app_state = AppState()