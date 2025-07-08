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
        self.main_branch = IntVar(root)  # Store the main branch number
        self.flowrate_entries = []  # Stores flow rates
        self.length_entries = []  # Stores lengths
        self.get_alt = IntVar(root)
        self.get_temp = IntVar(root)
        self.filename = StringVar(root)  # Store the filename
        self.diameter_values = []  # Store the diameter value
        self.friction_loss_per_length = []  # Store the friction loss value

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
        # PDF setup
        pdf_filename = app_state.filename.get() + ".pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

        # Header and footer text
        header = "A continuacion se muestran los resultados obtenidos del dimensionamiento de los ductos"
        footer = "[footer]"

        def draw_text(canvas, doc):
            width, height = letter
            canvas.drawString(80, height - 50, header)
            canvas.drawString(100, height - 700, footer)

        # Get data
        rows = app_state.duct_number.get()
        length_values = app_state.length_entries
        flowrate_values = app_state.flowrate_entries
        selected = app_state.selected_option.get()
        temperature = app_state.get_temp.get() if hasattr(app_state.get_temp, "get") else app_state.get_temp

        try:
            diameter_values = app_state.diameter_values
        except AttributeError:
            diameter_values = []

        try:
            friction_loss_per_length_values = app_state.friction_loss_per_length
        except AttributeError:
            friction_loss_per_length_values = []

        # Define header ONCE
        if selected == 1:
            data = [['Ramal', 'Caudal (L/s)', 'Longitud(m)', 'Temperatura(C°)', 'Presión(Pa)',
                    'Velocidad(m/s)', 'Pérdidas(Pa/m)', 'Diámetro(mm)']]
        elif selected == 2:
            data = [['Ramal', 'Caudal (m³/s)', 'Longitud(m)', 'Temperatura(C°)', 'Presión(Pa)',
                    'Velocidad(m/s)', 'Pérdidas(Pa/m)', 'Diámetro(mm)']]
        elif selected == 3:
            data = [['Ramal', 'Caudal (cfm)', 'Longitud(ft)', 'Temperatura(F°)', 'Presión(Pa)',
                    'Velocidad(fpm)', 'Pérdidas(inH20/ft)', 'Diámetro(in)']]

        # Build rows
        for i in range(rows):
            row_number = str(i + 1)
            flowrate = flowrate_values[i] if i < len(flowrate_values) else ''
            length = length_values[i] if i < len(length_values) else ''
            pressure = app_state.get_alt.get() if hasattr(app_state.get_alt, "get") else app_state.get_alt
            velocity = 2.48
            diameter = diameter_values[i] if i < len(diameter_values) else ''
            friction_loss = friction_loss_per_length_values[i] if i < len(friction_loss_per_length_values) else ''
            diameter = f"{diameter:.2f}" if diameter != '' else ''
            friction_loss = f"{friction_loss:.2f}" if friction_loss != '' else ''

            row = [row_number, flowrate, length, temperature, pressure, velocity, friction_loss, diameter]
            data.append(row)

        # Create and style the table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Build PDF
        doc.build([table], onFirstPage=draw_text)

        print(f"PDF '{pdf_filename}' created successfully!")
        
    # Button to generate PDF
    generate_pdf_btn = Button(middle_frame, text='Generar PDF con los resultados', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 25, 'bold'), command=generate_pdf)
    generate_pdf_btn.pack(side='top', pady=10)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=result1_menu)
    back_btn.pack(side='left', padx=10, pady=10)

    back_main_btn = Button(bottom_frame, text='Volver al menu principal', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=main_menu)
    back_main_btn.pack(side='right', pady=10)

##################################################################################################################################################
#function to switch to the results
def result1_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
        
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    pre_result_main = Label(top_frame, text='Dimensionamiento preliminar', font=('Arial', 30), bg='gray12', fg='gray80')
    pre_result_main.pack(side='top', pady=1)

    main_branch_lbl = Label(top_frame, text='El ramal principal se muestra en color rojo en la tabla', font=('Arial', 20), bg='gray12', fg='gray80')
    main_branch_lbl.pack(side='top', pady=1)

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
    

    # lists to store the results of diameter and friction loss per length
    diameter_values = []
    friction_loss_per_length_values = []

    density = 1.2  # kg/m³ at sea level (standard air)
    f = 0.0275  # typical roughness friction factor for ducts

    # Loop through each branch to calculate diameter and friction loss

    for i in range(len(flowrate_values)):
        flow_value = flowrate_values[i]
        length_value= length_values[i]  # still available if you need it

        if selected == 1:
            velocity = 2.47  # m/s
            Q = flow_value / 1000  # L/s → m³/s
            diameter_m = math.sqrt((4 * Q) / (math.pi * velocity)) # m
            diameter = diameter_m * 1000  # m → mm
            
            #f = 0.25 / [ math.log10( (ε / (3.7 * D)) + (5.74 / Re^0.9) ) ]^2  # friction factor for turbulent flow
            S = f * (1 / diameter_m) * (density * velocity ** 2) / 2  # Pa per meter

        elif selected == 2:
            velocity = 2.47  # m/s
            Q = flow_value  # m³/s
            diameter_m = math.sqrt((4 * Q) / (math.pi * velocity)) # m
            diameter = diameter_m * 1000  # m → mm

            S = f * (1 / diameter_m) * (density * velocity ** 2) / 2  # Pa per meter

        elif selected == 3:
            velocity = 2.47 * 196.85  # m/s → fpm
            Q_ft3s = flow_value / 60  # CFM → ft³/s
            A_ft2 = Q_ft3s / velocity  # fpm
            D_ft = math.sqrt((4 * A_ft2) / math.pi) # ft
            diameter_in = D_ft * 12  # ft → in
            diameter = diameter_in

            density_ip = 0.075  # lb/ft³ standard air
            f_ip = 0.0275   # typical roughness friction factor for ducts in imperial units

            S_ip = f_ip * (1 / D_ft) * (density_ip * velocity ** 2) / 2  # lb/ft² per ft
            S = S_ip / 5.202  # convert lb/ft² to in.wg per ft

        else:
            diameter = None
            S = None

        diameter_values.append(diameter)
        friction_loss_per_length_values.append(S)
        
        app_state.diameter_values = diameter_values  # Store the diameter values in app_state
        app_state.friction_loss_per_length = friction_loss_per_length_values  # Store the friction loss values in app_state

        
    # Create labels for the results
    
    # Number of each branch and highlight the main branch
    for i in range(rows):
            if app_state.main_branch.get() == i + 1: 
                branch_values = Label(middle_frame, text=f"Ramal {i+1}", width=7, height=1, 
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='red3')
                branch_values.grid(row=i+1, column=0, padx=2, pady=2, sticky="nsew")
            else:
                branch_values = Label(middle_frame, text=f"Ramal {i+1}", width=7, height=1, 
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
                branch_values.grid(row=i+1, column=0, padx=2, pady=2, sticky="nsew")
    
    #these for statemnts shows the value of the flowrate, length, temperature, pressure etc; the correct units to display are set in the below if statement.
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
    
    for i in range(rows):
            velocity_value = 2.48  # m/s
            branch_velocity_values = Label(middle_frame, text=f"{velocity_value:.2f}", width=7, height=1,
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
            branch_velocity_values.grid(row=i+1, column=5, padx=2, pady=2, sticky="nsew")

    for i in range(rows):
            friction_loss_value = friction_loss_per_length_values[i]
            branch_friction_loss_values = Label(middle_frame, text=f"{friction_loss_value:.2f}", width=7, height=1,
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
            branch_friction_loss_values.grid(row=i+1, column=6, padx=2, pady=2, sticky="nsew")
            
    for i in range(rows):
            diameter_value = diameter_values[i]  # Get the diameter value from the list
            branch_diameter_values = Label(middle_frame, text=f"{diameter_value:.2f}", width=7, height=1,
                            borderwidth=2, relief="solid", font=('Arial', 15), bg='gray12', fg='gray80')
            branch_diameter_values.grid(row=i+1, column=7, padx=2, pady=2, sticky="nsew")

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
        if app_state.main_branch.get() == i + 1:
            Label(middle_frame, text=f'Ramal {i+1} (Principal):', font=('Arial', 14), bg='grey12', fg='red3').grid(row=i+1, column=0, padx=3, pady=1)
        else:
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
    
    #top frame for the menu title
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    # Title for the duct information menu
    duct_info_tittle = Label(top_frame, text='Complete la información sobre los ramales \n del sistema, luego presione " Siguiente".', font=('Arial', 30, 'bold'), bg='gray12', fg='gray80')
    duct_info_tittle.pack(pady=10)
    
    # Entry for branch number and main branch
    # Middle frame to hold entry fields
    middle_frame = Frame(W, bg='gray12')
    middle_frame.pack(expand=True)

    duct_number_lbl = Label(middle_frame, text='Introduzca la cantidad de ramales del ducto. ', font=('Arial', 26), bg='gray12', fg='gray80')
    duct_number_lbl.pack(pady=1)

    duct_number_entry = Entry(middle_frame, font=('Arial', 15), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
    duct_number_entry.pack(pady=20, ipady=5, ipadx=10)

    main_branch_lbl = Label(middle_frame, text='Introduzca el número de ramal que va a usar \n como ramal principal:', font=('Arial', 26), bg='gray12', fg='gray80')
    main_branch_lbl.pack(pady=5)

    main_branch_entry = Entry(middle_frame, font=('Arial', 15), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
    main_branch_entry.pack(pady=20, ipady=5, ipadx=10)

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
    
    #funcion to save the main branch number
    def save_main_branch():
        value = main_branch_entry.get()
        if value == 'Escribe aquí...':
            app_state.main_branch.set(0)
        else:
            try:
                app_state.main_branch.set(int(value))
            except ValueError:
                print("Error: Ingrese un número válido")
        print(f'El ramal principal es el número: {app_state.main_branch.get()}')  # Verify it's working
    # Button to save the duct number and main branch
        
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='Brown4', font=('Arial', 20, 'bold'), command=file_name_menu)
    back_btn.pack (side='left', padx=10, pady=10)

    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='Brown4', font=('Arial', 20, 'bold'), command=lambda: [save_duct_number(), save_main_branch(), units_menu()])
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
