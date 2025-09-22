from tkinter import Button, Label, Radiobutton, StringVar
from app_state import app_state

def units_menu(W, go_back):
    for widget in W.winfo_children():
        widget.destroy()

    lbl = Label(W, text="Seleccione las unidades:", bg="gray12", fg="gray80", font=("Arial", 20))
    lbl.pack(pady=20)

    units_var = StringVar(W, value="SI")

    Radiobutton(W, text="Sistema Internacional (SI)", variable=units_var, value="SI").pack(anchor="w", padx=40, pady=5)
    Radiobutton(W, text="Sistema Imperial (IP)", variable=units_var, value="IP").pack(anchor="w", padx=40, pady=5)

    def save_units():
        app_state.selected_option.set(units_var.get())
        print("Unidades seleccionadas:", app_state.selected_option.get())

    save_btn = Button(W, text="Guardar", command=save_units)
    save_btn.pack(pady=10)

    back_btn = Button(W, text="← Volver", command=lambda: go_back(W))
    back_btn.pack(side="left", padx=20, pady=20)