#this is a sketch for the new menus, before inserted into the main file, try this code in a separate file

#setttings and libraries
from tkinter import Tk, Label, Button, Entry, Frame, IntVar, StringVar# importar libreria tkinter para crear la interfaz grafica
import math  # importar libreria para operaciones matematicas
from reportlab.lib.pagesizes import letter # importar libreria para crear el pdf
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle 
from reportlab.lib import colors

class AppState:
    def __init__(self, root):
        self.selected_option = IntVar(root)  # Attach variable to Tkinter root(que los valores de las varibles se guarden para utilizarlos en otras funciones)
        self.duct_number = IntVar(root)  # Store the number of ducts
        self.flowrate_entries = []  # Stores flow rates
        self.length_entries = []  # Stores lengths
        self.get_alt = IntVar(root)
        self.get_temp = IntVar(root)
        self.filename = StringVar(root)  # Store the filename

W = Tk()
W.title('Dimensionamiento de Ductos')
W.geometry('1200x800')
W.config(bg='gray12')

app_state = AppState(W)


    #THIS ARE THE CALCULATIONS FOR FRICTION LOSSES USING EQUAL FRICTION METHOD
    #rho = 1.2  # Density of air in kg/m³
    #mu = 1.81e-5  # Dynamic viscosity of air in kg/(m·s)
    #nu = mu / rho  # Kinematic viscosity in m²/s
    #D = 0.6  # Diameter in meters
    #L = 30  # Length in meters
    #V = 8.85  # Velocity in m/s
    #eps = 0.00009 #roughness of the duct in meters for galvanized steel 
    #Re = (rho * V * D) / mu  # Reynolds number
    
    
    
    # If statement for turbulent or laminar flow
    #if Re > 2000:
        #f = 1 / (-1.8 * math.log10(6.9 / Re + (eps / (3.7 * D)) ** 1.11)) ** 2 #turbulent flow
    #else:
        #f = 64/Re #laminar flow
    
    #deltaP = f * (L/D) * (rho * V**2) / 2
    #print(f"Reynolds number: {Re}")
    #print(f"Friction factor: {f}")
    #print(f"Pressure loss due to friction: {deltaP} Pa")






def main_menu():
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()

    # Original Main Menu
    lbl1 = Label(W, text='DIMENSIONAMIENTO DE DUCTOS \n DE AIRE ACONDICIONADO', font=('Arial', 30, 'bold'), bg='gray12', fg='brown2')
    lbl1.pack(pady=1)
    
    lbl2 = Label(W, text='Con este programa usted podrá dimensionar ductos de ventilación \n considerando las pérdidas debidas a la fricción en tramos rectos y \n en accesorios. Solo es necesario conocer el caudal en los \n ramales del sistema. Además, el programa presenta los ductos \n rectangulares equivalentes.', font=('Arial', 26), bg='gray12', fg='gray80')
    lbl2.pack(pady=1)

    lbl3 = Label(W, text='(En los cálculos se incluyen las correcciones debidas a la altitud, \n la temperatura y la rugosidad.)', font=('Arial', 16), bg='gray12', fg='gray80')
    lbl3.pack(pady=1)
    
    #start_button = Button(W, text='Iniciar', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 24, 'bold'), command=sketch_menu)
    #start_button.pack(pady=30)

    lbl5 = Label(W, text='Desarrollado en la Universidad del Valle por Luis Jimenez', font=('Arial', 12, 'bold'), bg='gray12', fg='gray80')
    lbl5.pack(side='bottom', pady=1)

main_menu()


W.mainloop()