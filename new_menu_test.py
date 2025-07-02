#el orden de el codigo  es el siguiente: settings_menu3(units) -> menu2(duct_number) -> menu1(filename) -> main_menu
#cada menu tiene un boton para volver al menu anterior y otro para ir al siguiente menu
#el menu 1 tiene un boton para guardar el nombre del archivo que se va a crear

###################################################################################################################################
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

###################################################################################################################################
#function to switch to roughness menu
def rectangular_eq_menu():
    for widget in W.winfo_children():
        widget.destroy()
    
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    rectangular_lbl = Label(top_frame, text='Las dimensiones para los ductos rectangulares equivalentes \n de cada ramal del sistema se presenta a continuación', font=('Arial', 25), bg='gray12', fg='gray80')
    rectangular_lbl.pack(side='top', pady=1)
    
    middle_frame = Frame(W, bg='gray12',highlightbackground="red", highlightthickness=2)
    middle_frame.pack(expand=True)
    
    selected =  app_state.selected_option.get()
    rows_number = app_state.duct_number.get()
    rows, cols = rows_number, 3
    
    for i in range(rows):
        branch_values = Label(middle_frame, text=f"Ramal {i+1}", width=7, height=1, 
                        borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
        branch_values.grid(row=i+1, column=0, padx=2, pady=2, sticky="nsew")
    
    #if statement to show the correct units for the rectangular equivalent menu
    if selected == 1:
        rect_eq_1_lbl = Label(middle_frame, text='opción 1 (m)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_1_lbl.grid(row=0, column=1)
        
        rect_eq_2_lbl = Label(middle_frame, text='opción 2 (m)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_2_lbl.grid(row=0, column=2)
        
        rect_eq_3_lbl = Label(middle_frame, text='opción 3 (m)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_3_lbl.grid(row=0, column=3)
    
    elif selected == 2:
        rect_eq_1_lbl = Label(middle_frame, text='opción 1 (m)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_1_lbl.grid(row=0, column=1)
        
        rect_eq_2_lbl = Label(middle_frame, text='opción 2 (m)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_2_lbl.grid(row=0, column=2)
        
        rect_eq_3_lbl = Label(middle_frame, text='opción 3 (m)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_3_lbl.grid(row=0, column=3)
    
    elif selected == 3:
        rect_eq_1_lbl = Label(middle_frame, text='opción 1 (in)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_1_lbl.grid(row=0, column=1)
        
        rect_eq_2_lbl = Label(middle_frame, text='opción 2 (in)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_2_lbl.grid(row=0, column=2)
        
        rect_eq_3_lbl = Label(middle_frame, text='opción 3 (in)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        rect_eq_3_lbl.grid(row=0, column=3)
        
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=corrections_menu)
    back_btn.pack (side='left', padx=10, pady=10)

###################################################################################################################################
#function to switch to roughness menu
def roughness_menu():
    for widget in W.winfo_children():
        widget.destroy()

    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    middle_frame = Frame(W, bg='gray12')
    middle_frame.pack(expand=True)
    
    roughness_lbl = Label(top_frame, text='Hasta ahora se ha trabajado con una rugosidad #### \n Seleccione el material del ducto', font=('Arial', 25), bg='gray12', fg='gray80')
    roughness_lbl.pack(side='top', pady=1)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=corrections_menu)
    back_btn.pack (side='left', padx=10, pady=10)
    

###################################################################################################################################

#function to switch corrections menu
def corrections_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
        
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    corrections_lbl = Label(top_frame, text='Menú de correcciones', font=('Arial', 30), bg='gray12', fg='gray80')
    corrections_lbl.pack(side='top', pady=1)
    
    middle_frame = Frame(W, bg='gray12')
    middle_frame.pack(expand=True)
    
    ruogosity_btn = Button(middle_frame, text='Correcion por rugosidad del material del ducto', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 25, 'bold'), command=roughness_menu)
    ruogosity_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    rectangular_eq_btn = Button(middle_frame, text='Ductos rectangulares equivalentes', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 25, 'bold'),command=rectangular_eq_menu)
    rectangular_eq_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    pre_desing_btn = Button(middle_frame, text='Volver a hacer el dimensionamiento preliminar', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 25, 'bold'))
    pre_desing_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    # Function to generate the PDF
    def generate_pdf():
        # Call the function to create the PDF
        # PDF setup
        pdf_filename = app_state.filename.get() + ".pdf"  # Use the filename from app_state
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
        
        # Header and footer text
        header = "A continuacion se muestran los resultados obtenidos del dimensionamiento de los ductos"
        footer = "[footer]"

        
        # Text drawing function
        def draw_text(canvas, doc):
            width, height = letter
            canvas.drawString(80, height - 50, f"{header}") 
            canvas.drawString(100, height - 700, f"{footer}")
        
        
        # Get the number of rows and the values of each app from app_state
        rows = app_state.duct_number.get()
        length_values = app_state.length_entries
        flowrate_values = app_state.flowrate_entries
        selected = app_state.selected_option.get()
        
        if selected == 1:
            # Table data (like an Excel sheet) using right dimensions
            data = [['Ramal', 'Caudal (L/s)', 'Longitud(m)', 'Temperatura(C°)', 'Presión(Pa)', 'Diámetro(mm)', 'Velocidad(m/s)', 'Pérdidas(Pa/m)']]
        elif selected == 2:
            data = [['Ramal', 'Caudal (m³/s)', 'Longitud(m)', 'Temperatura(C°)', 'Presión(Pa)', 'Diámetro(mm)', 'Velocidad(m/s)', 'Pérdidas(Pa/m)']]
        elif selected == 3:
            data = [['Ramal', 'Caudal (cfm)', 'Longitud(ft)', 'Temperatura(F°)', 'Presión(Pa)', 'Diámetro(in)', 'Velocidad(fpm)', 'Pérdidas(inH20/ft)']]
        
        # Build table rows
        for i in range(rows):
            row_number = str(i + 1)

            # Get values or fallback to empty strings
            flowrate = flowrate_values[i] if i < len(flowrate_values) else ''
            length = length_values[i] if i < len(length_values) else ''

            # Fill in only 'Caudal' (index 1) and 'Longitud' (index 2), rest are empty
            row = [row_number, flowrate, length, '', '', '', '', '']
            data.append(row)

        # Create table and style
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build PDF with table and text
        doc.build([table], onFirstPage=draw_text)

        print(f"PDF '{pdf_filename}' created successfully!")

    # Button to generate the PDF
    show_results_btn = Button(middle_frame, text='Mostrar resultados', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 25, 'bold'), command=generate_pdf)
    show_results_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    # Create a button to calculate accessories
    accesories_btn = Button(middle_frame, text='Calcular Accesorios', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 25, 'bold'))
    accesories_btn.pack(padx=5, pady=5, anchor="w", fill="x")
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=result1_menu)
    back_btn.pack (side='left', padx=10, pady=10)   
    

###################################################################################################################################
#function to switch to the results
def result1_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
        
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    pre_result_main = Label(top_frame, text='Dimensionamiento preliminar', font=('Arial', 30), bg='gray12', fg='gray80')
    pre_result_main.pack(side='top', pady=1)

    middle_frame = Frame(W, bg='gray12',highlightbackground="red", highlightthickness=2)
    middle_frame.pack(expand=True)
    
    #Get values from the entry fields
    
    selected =  app_state.selected_option.get()
    rows_number = app_state.duct_number.get()
    T = float(app_state.get_temp)
    
    print(f"Selected option: {selected}")
    print(f"Duct number: {rows_number}")
    rows, cols = rows_number, 6
    
    #function that calculates the pressure at a given altitude
    def calculate_pressure(H):
        # Constants
        P0 = 101325  # Sea-level standard atmospheric pressure (Pa)
        factor = 0.0000225577  # Altitude factor
        exponent = 5.2559  # Exponent for the equation
    
        # Pressure formula
        P = P0 * (1 - factor * H) ** exponent
    
        return P
        
    # set the altitude to the value of the entry
    H = float(app_state.get_alt)
    # Calculate pressure
    pressure = calculate_pressure(H)
    
    #variables to get the values of the flowrate and length
    flowrate_values = app_state.flowrate_entries
    length_values = app_state.length_entries
    
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

    # Number of each branch
    for i in range(rows):
            branch_values = Label(middle_frame, text=f"Ramal {i+1}", width=7, height=1, 
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
            branch_values.grid(row=i+1, column=0, padx=2, pady=2, sticky="nsew")
    
    #these for statemnts shows the value of the flowrate, length, temperature and pressure; the correct units to display are set in the below if statement.
    for i in range(len(flowrate_values)):
            flow_value = flowrate_values[i]  # Get the entered text from Entry
            branch_flow_values = Label(middle_frame, text=f"{flow_value}", width=7, height=1, 
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
            branch_flow_values.grid(row=i+1, column=1, padx=2, pady=2, sticky="nsew")
    
    for i in range(len(length_values)):
            length_value = length_values[i]  # Get the entered text from Entry
            branch_length_values = Label(middle_frame, text=f"{length_value}", width=7, height=1, 
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
            branch_length_values.grid(row=i+1, column=2, padx=2, pady=2, sticky="nsew")
            
    for i in range(rows):
            branch_temperature_values = Label(middle_frame, text=f"{T}", width=7, height=1, 
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
            branch_temperature_values.grid(row=i+1, column=3, padx=2, pady=2, sticky="nsew")
    
    for i in range(rows):
            branch_pressure_values = Label(middle_frame, text=f"{pressure:.2f}", width=7, height=1, 
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
            branch_pressure_values.grid(row=i+1, column=4, padx=2, pady=2, sticky="nsew")
    
    if selected == 1:
        flowrate_main = Label(middle_frame, text='Caudal (L/s)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        flowrate_main.grid(row=0, column=1)
        
        length_main = Label(middle_frame, text='Longitud (m)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        length_main.grid(row=0, column=2)
        
        temperatue_main = Label(middle_frame, text='Temperatura (C°)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        temperatue_main.grid(row=0, column=3)
        
        preasure_main = Label(middle_frame, text='Presión (Pa)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        preasure_main.grid(row=0, column=4)
        
        velocity_main = Label(middle_frame, text='Velocidad (m/s)', font=('Arial', 15),highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        velocity_main.grid(row=0, column=5)       
        
        friction_loses_main = Label(middle_frame, text='Pérdidas por fricción (Pa/m)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        friction_loses_main.grid(row=0, column=6)
        
        diameter_main = Label(middle_frame, text='Diámetro (mm)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        diameter_main.grid(row=0, column=7)       
        
    elif selected == 2:
        flowrate_main = Label(middle_frame, text='Caudal (m³/s)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        flowrate_main.grid(row=0, column=1)
        
        length_main = Label(middle_frame, text='Longitud (m)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        length_main.grid(row=0, column=2)
        
        temperatue_main = Label(middle_frame, text='Temperatura (C°)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        temperatue_main.grid(row=0, column=3)
        
        preasure_main = Label(middle_frame, text='Presión (Pa)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        preasure_main.grid(row=0, column=4)
        
        velocity_main = Label(middle_frame, text='Velocidad (m/s)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        velocity_main.grid(row=0, column=5)       
        
        friction_loses_main = Label(middle_frame, text='Pérdidas por fricción (Pa/m)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        friction_loses_main.grid(row=0, column=6)
        
        diameter_main = Label(middle_frame, text='Diámetro (mm)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        diameter_main.grid(row=0, column=7) 
        
    elif selected == 3:
        flowrate_main = Label(middle_frame, text='Caudal (cfm)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        flowrate_main.grid(row=0, column=1)
        
        length_main = Label(middle_frame, text='Longitud (ft)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        length_main.grid(row=0, column=2)
        
        temperatue_main = Label(middle_frame, text='Temperatura (F°)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        temperatue_main.grid(row=0, column=3)
        
        preasure_main = Label(middle_frame, text='Presión (Pa)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        preasure_main.grid(row=0, column=4)
        
        velocity_main = Label(middle_frame, text='Velocidad (fpm)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        velocity_main.grid(row=0, column=5)       
        
        friction_loses_main = Label(middle_frame, text='Pérdidas por fricción (inH20/ft)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        friction_loses_main.grid(row=0, column=6)
        
        diameter_main = Label(middle_frame, text='Diámetro (in)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        diameter_main.grid(row=0, column=7) 
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    try_another_speed = Button (bottom_frame, text='Intentar con otra velocidad', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=velocity_range_menu) 
    try_another_speed.pack(side='left', padx=10, pady=10)
    
    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'),  command=corrections_menu)
    next_btn.pack(side='right' , padx= 10, pady=10)
    
###################################################################################################################################

#function to switch to the velocity range menu
def velocity_range_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
    #altitude and temperature menu interface
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    ASHRAE_vel_rec_lbl = Label(top_frame, text='Recomendación ASHRAE', font=('Arial', 24, 'bold'), bg='gray12', fg='gray80')
    ASHRAE_vel_rec_lbl.pack(side='top', pady=1)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=branches_features)
    back_btn.pack (side='left', padx=10, pady=10)

    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=result1_menu)
    next_btn.pack(side='right' , padx= 10, pady=10)

###################################################################################################################################

# Function to save flow rate and length values to app_state
def save_branch_data():
    """Save the flow rate and length for each branch in app_state."""
    app_state.flowrate_entries = []  # Reset stored values
    app_state.length_entries = []

    for i in range(app_state.duct_number.get()):
        try:
            flowrate = float(flowrate_entries[i].get())  # Convert input to float
            length = float(length_entries[i].get())

            app_state.flowrate_entries.append(flowrate)
            app_state.length_entries.append(length)
        except ValueError:
            print(f"Error: Ingrese valores válidos en el Ramal {i+1}")

    print("Caudales guardados:", app_state.flowrate_entries)
    print("Longitudes guardadas:", app_state.length_entries)

# Function to create the menu for branch features
def branches_features():
    """Create a menu with input fields for flow rate and length of each branch."""
    global middle_frame, flowrate_entries, length_entries
    for widget in W.winfo_children():
        widget.destroy()

    Label(W, text="Ingrese los valores de caudal y longitud de ramal", font=('Arial', 30, 'bold'), bg='grey12', fg='grey80').pack(pady=10)

    selected = app_state.selected_option.get()
    duct_number = app_state.duct_number.get()

    # Frame to hold entry fields
    middle_frame = Frame(W, bg='grey12')
    middle_frame.pack(pady=10)

    app_state.flowrate_entries = []  # Reset stored values
    app_state.length_entries = []

    # Header Labels
    headers = {
        1: ("Caudal (L/s)", "Longitud (m)"),
        2: ("Caudal (m³/h)", "Longitud (m)"),
        3: ("Caudal (cfm)", "Longitud (ft)")
    }
    
    if selected in headers:
        Label(middle_frame, text=headers[selected][0], font=('Arial', 16,'bold'), bg='grey12', fg='grey80').grid(row=0, column=1, padx=5, pady=5)
        Label(middle_frame, text=headers[selected][1], font=('Arial', 16,'bold'), bg='grey12', fg='grey80').grid(row=0, column=2, padx=5, pady=5)

    # Create input fields for each branch
    flowrate_entries = []
    length_entries = []

    for i in range(duct_number):
        Label(middle_frame, text=f'Ramal {i+1}:', font=('Arial', 14), bg='grey12', fg='white').grid(row=i+1, column=0, padx=3, pady=1)

        flowrate_entry = Entry(middle_frame, font=('Arial', 12), bg='grey40', width=10)
        flowrate_entry.grid(row=i+1, column=1, padx=5, pady=1)
        flowrate_entries.append(flowrate_entry)

        length_entry = Entry(middle_frame, font=('Arial', 12), bg='grey40' , width=10)
        length_entry.grid(row=i+1, column=2, padx=5, pady=1)
        length_entries.append(length_entry)
    
        # Placeholder text
    placeholder = 'Escribe aquí...'
    flowrate_entry.insert(0, placeholder)

    # Functions to handle placeholder behavior
    def on_focus_in(event):
        if flowrate_entry.get() == placeholder:
            flowrate_entry.delete(0, 'end')
            flowrate_entry.config(fg='black')

    def on_focus_out(event):
        if flowrate_entry.get() == '':
            flowrate_entry.insert(0, placeholder)
            flowrate_entry.config(fg='gray')

    # Bind focus events
    flowrate_entry.bind('<FocusIn>', on_focus_in)
    flowrate_entry.bind('<FocusOut>', on_focus_out)

    # Auto-focus for caret visibility
    flowrate_entry.focus()
        
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=altitude_temperature_menu)
    back_btn.pack (side='left', padx=10, pady=10)

    save_btn = Button(bottom_frame, text="Guardar y Continuar", bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold') ,command= lambda: [save_branch_data(),velocity_range_menu()])
    save_btn.pack (side ='right', padx=10, pady=10)
###################################################################################################################################

#function to switch to the altitude and temperature menu
def altitude_temperature_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
        
    #altitude and temperature menu interface
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    alt_temp_lbl = Label(top_frame, text=' Ingrese la altitud y temperatura del \n lugar de la instalación', font=('Arial', 30), bg='gray12', fg='gray80')
    alt_temp_lbl.pack(side='top', pady=1)
    
    #middel frame to hold entry fields
    middle_frame = Frame(W, bg='gray12')
    middle_frame.pack(expand=True)
    
    selected = app_state.selected_option.get()
    
    if selected == 3:

        temp_lbl = Label(middle_frame, text='Temperatura (F°)', font=('Arial', 25, 'bold'), bg='gray12', fg='gray80')
        temp_lbl.grid(row=1, column=0)
        temp_entry = Entry(middle_frame, font=('Arial', 15), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
        temp_entry.grid(row=1, column=1)
    
        alt_lbl = Label(middle_frame, text='Altitud (ft)', font=('Arial', 25, 'bold'), bg='gray12', fg='gray80')
        alt_lbl.grid(row=0, column=0)
        alt_entry = Entry(middle_frame, font=('Arial', 15), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
        alt_entry.grid(row=0, column=1)
    
    else:
        temp_lbl = Label(middle_frame, text='Temperatura (C°)', font=('Arial', 25, 'bold'), bg='gray12', fg='gray80')
        temp_lbl.grid(row=1, column=0)
        temp_entry = Entry(middle_frame, font=('Arial', 15), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
        temp_entry.grid(row=1, column=1)
    
        alt_lbl = Label(middle_frame, text='Altitud (m)', font=('Arial', 25, 'bold'), bg='gray12', fg='gray80')
        alt_lbl.grid(row=0, column=0)
        alt_entry = Entry(middle_frame, font=('Arial', 15), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
        alt_entry.grid(row=0, column=1)       
    
    
    # Placeholder text
    placeholder = 'Escribe aquí...'
    alt_entry.insert(0, placeholder)

    # Functions to handle placeholder behavior
    def on_focus_in(event):
        if alt_entry.get() == placeholder:
            alt_entry.delete(0, 'end')
            alt_entry.config(fg='black')

    def on_focus_out(event):
        if alt_entry.get() == '':
            alt_entry.insert(0, placeholder)
            alt_entry.config(fg='gray')

    # Bind focus events
    alt_entry.bind('<FocusIn>', on_focus_in)
    alt_entry.bind('<FocusOut>', on_focus_out)

    # Auto-focus for caret visibility
    alt_entry.focus()
    
    # Function to get values from entry fields
    def get_values():
        app_state.get_alt = alt_entry.get()
        app_state.get_temp = temp_entry.get()
        print(f"Altitude: {app_state.get_alt}, Temperature: {app_state.get_temp}")  # Print values to check
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=units_menu)
    back_btn.pack (side='left', padx=10, pady=10)

    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=lambda: [get_values(), branches_features()])
    next_btn.pack(side='right' , padx= 10, pady=10)


###################################################################################################################################
#function to switch to the units menu
def units_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
        
    #menu 3 interface
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    menu3_lbl = Label(top_frame, text='El programa permite escoger entre tres sistemas \n de unidades. Seleccione las unidades para: caudal, \n pérdidas, diámetro y velocidad, respectivamente.', font=('Arial', 30), bg='gray12', fg='gray80')
    menu3_lbl.pack(side='top', pady=1)
    
    guide_lbl = Label(top_frame, text='(haga clic en una de las opciones, luego presione siguiente)', font=('Arial', 18), bg='gray12', fg='gray80')
    guide_lbl.pack(side='top', pady=1)
    
    #selecion de unidades
    middle_frame = Frame(W, bg='gray12')
    middle_frame.pack(expand=True)
    
    unidades_lbl = Label(middle_frame, text='UNIDADES', font=('Arial', 25, 'bold'), bg='gray12', fg='gray80')
    unidades_lbl.grid(row=0, column=2)

    # Function to update button selection
    def select_option(value):
        app_state.selected_option.set(value)
        print(f"Selected option: {value}")

        # Update button colors based on selection
        for i, btn in enumerate(buttons, start=1):
            if i == value:
                btn.config(bg="lightblue")  # Highlight the selected button
            else:
                btn.config(bg="DarkSlateGray")  # Reset others to default

    # Create buttons and store them in a list
    buttons = [
        Button(middle_frame, text='1. L/s    :   Pa/m   : mm : m/s : m ', bg='DarkSlateGray', fg='black',
                relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4',
                font=('Arial', 20, 'bold'), command=lambda: select_option(1)),

        Button(middle_frame, text='2. m³/s :   Pa/m   : mm : m/s : m ', bg='DarkSlateGray', fg='black',
                relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4',
                font=('Arial', 20, 'bold'), command=lambda: select_option(2)),

        Button(middle_frame, text='3. cfm    : inH20/ft : in : fpm : ft', bg='DarkSlateGray', fg='black',
                relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4',
                font=('Arial', 20, 'bold'), command=lambda: select_option(3))  
    ]

    # Place buttons in the grid
    for i, btn in enumerate(buttons, start=1):
        btn.grid(row=i, column=2, padx=5, pady=10, sticky='ew')
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=duct_number_menu)
    back_btn.pack (side='left', padx=10, pady=10)

    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'),  command=altitude_temperature_menu)
    next_btn.pack(side='right' , padx= 10, pady=10)


###################################################################################################################################
#function to switch to the duct number menu

def duct_number_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
    
    # Entry for duct number
    duct_number_lbl = Label(W, text='Introduzca la cantidad de ramales del ducto, luego \n presione siguiente:', font=('Arial', 30), bg='gray12', fg='gray80')
    duct_number_lbl.pack(pady=1)

    duct_number_entry = Entry(W, font=('Arial', 15), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
    duct_number_entry.pack(pady=10, ipady=5, ipadx=10)

    # Placeholder text for duct number
    duct_number_placeholder = 'Escribe aquí...'
    duct_number_entry.insert(0, duct_number_placeholder)

    # Functions to handle placeholder behavior
    def on_focus_in(event):
        if duct_number_entry.get() == duct_number_placeholder:
            duct_number_entry.delete(0, 'end')
            duct_number_entry.config(fg='black')

    def on_focus_out(event):
        if duct_number_entry.get() == '':
            duct_number_entry.insert(0, duct_number_placeholder)
            duct_number_entry.config(fg='gray')

    # Bind focus events
    duct_number_entry.bind('<FocusIn>', on_focus_in)
    duct_number_entry.bind('<FocusOut>', on_focus_out)

    # Auto-focus for caret visibility
    duct_number_entry.focus()

    # Function to save duct number using app_state
    def save_duct_number():
        value = duct_number_entry.get()  # Get the user input

        if value == duct_number_placeholder:
            app_state.duct_number.set(0)  # Avoid saving placeholder
        else:
            try:
                app_state.duct_number.set(int(value))  # Convert and store in app_state
            except ValueError:
                print("Error: Ingrese un número válido")  # Handle invalid input

        print(f'El número de ductos es: {app_state.duct_number.get()}')  # Verify it's working
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='Brown4', font=('Arial', 20, 'bold'), command=file_name_menu)
    back_btn.pack (side='left', padx=10, pady=10)

    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='Brown4', font=('Arial', 20, 'bold'), command=lambda: [save_duct_number(), units_menu()])
    next_btn.pack(side='right' , padx= 10, pady=10)

###################################################################################################################################

# function to switch to the file name menu
def file_name_menu():
    # Clear the current window
    for widget in W.winfo_children():
        widget.destroy()
    
    # New Menu Interface
    
    # Entry for file name
    file_name_lbl = Label(W, text='El programa va a crear un archivo con los \n resultados. Introduzca el nombre con el que \n desea guardar el archivo y presione "Guardar\n nombre del archivo", luego presione “Siguiente”:', font=('Arial', 26), bg='gray12', fg='gray80')
    file_name_lbl.pack(pady=1)

    file_name_entry = Entry(W, font=('Arial', 12), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
    file_name_entry.pack(pady=5, ipady=5, ipadx=10)

    # Placeholder text
    placeholder = 'Escribe aquí...'
    file_name_entry.insert(0, placeholder)

    # Functions to handle placeholder behavior
    def on_focus_in(event):
        if file_name_entry.get() == placeholder:
            file_name_entry.delete(0, 'end')
            file_name_entry.config(fg='black')

    def on_focus_out(event):
        if file_name_entry.get() == '':
            file_name_entry.insert(0, placeholder)
            file_name_entry.config(fg='gray')

    # Bind focus events
    file_name_entry.bind('<FocusIn>', on_focus_in)
    file_name_entry.bind('<FocusOut>', on_focus_out)
    
    # Auto-focus for caret visibility
    file_name_entry.focus()

    def save_filename():
        filename = file_name_entry.get()
    
        if filename == placeholder or filename.strip() == "":
            print("Nombre de archivo inválido.")
        else:
            app_state.filename.set(filename)  # Save the value
            print(f"Guardando como: {app_state.filename.get()}")  # Print to verify
        
    save_btn = Button(W, text='Guardar nombre del archivo', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=save_filename)
    save_btn.pack(pady=10)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=main_menu)
    back_btn.pack(side='left', padx=10, pady=10)

    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=duct_number_menu)
    next_btn.pack(side='right' , padx= 10, pady=10)


###################################################################################################################################
# Function to return to the main menu
# menu principal
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
    
    start_button = Button(W, text='Iniciar', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 24, 'bold'), command=file_name_menu)
    start_button.pack(pady=30)

    lbl5 = Label(W, text='Desarrollado en la Universidad del Valle por Luis Jimenez', font=('Arial', 12, 'bold'), bg='gray12', fg='gray80')
    lbl5.pack(side='bottom', pady=1)

main_menu()

W.mainloop()
