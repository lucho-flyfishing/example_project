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
        self.velocity_entries = []  # Stores velocities
        self.get_alt = IntVar(root)
        self.get_temp = IntVar(root)
        self.filename = StringVar(root)  # Store the filename
        self.diameter_values = []  # Store the diameter value
        self.friction_loss_per_length = []  # Store the friction loss value
        self.pressure = IntVar(root)
        self.density = None
        self.viscosity = None

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
    
    roughness_top_lbl = Label(top_frame, text='Hasta ahora se ha trabajado con una rugosidad #### \n Seleccione el material del ducto', font=('Arial', 25), bg='gray12', fg='gray80')
    roughness_top_lbl.pack(side='top', pady=1)
    
    middle_frame = Frame(W, bg='gray12',highlightbackground="red", highlightthickness=2)
    middle_frame.pack(expand=True)
    
    title_lbl = Label(middle_frame, text='Factores de rugosidad para el material del ducto', font=('Arial', 20, 'bold'),  borderwidth=2, relief="solid",bg='gray12', fg='gray80')
    title_lbl.grid(row=0, column=0, columnspan=3, padx=5, pady=3, sticky="nsew")
    
    material_lbl = Label(middle_frame, text='Material', font=('Arial', 15), bg='gray12', fg='gray80')
    material_lbl.grid(row=1, column=0, padx=5, pady=3, sticky="nsew")
    
    category_lbl = Label(middle_frame, text='Categoría', font=('Arial', 15), bg='gray12', fg='gray80')
    category_lbl.grid(row=1, column=1, padx=5, pady=3, sticky="nsew")

    selected =  app_state.selected_option.get()
    
    if selected == 3:
    
        table1_roughness_imperial = [
            ["Lisa", 0.00118],  
            ["Lisa", 0.00118],
            ["Lisa", 0.00118],
            ["Lisa", 0.00118],   
            ["Medianamente Lisa", 0.00354],
            ["Promedio", 0.00591],
            ["Promedio", 0.00591],  
            ["Medianamente Rugosa", 0.03543],
            ["Medianamente Rugosa", 0.03543],
            ["Rugosa", 0.11811],
            ["Medianamente Rugosa", 0.03543],
            ["Rugosa", 0.11811],
            ["Rugosa", 0.11811],
            ["Rugosa", 0.11811],
            ["Rugosa", 0.11811],
        ]

        for i, row in enumerate(table1_roughness_imperial):
            for j, value in enumerate(row):
                label = Label(middle_frame, text=value, borderwidth=1, relief="solid", width=16, height=1)
                label.grid(row=i+2, column=j+1, padx=2, pady=2)
    

        roughness_imp_lbl = Label(middle_frame, text='Factor de Rugosidad (in)', font=('Arial', 15), bg='gray12', fg='gray80')
        roughness_imp_lbl.grid(row=1, column=2, padx=5, pady=3, sticky="nsew")
    
    else:
        
        table2_roughness = [
            ["Lisa", 0.03],  
            ["Lisa", 0.03],
            ["Lisa", 0.03],
            ["Lisa", 0.03],   
            ["Medianamente Lisa", 0.09],
            ["Promedio", 0.15],
            ["Promedio", 0.15],  
            ["Medianamente Rugosa", 0.9],
            ["Medianamente Rugosa", 0.9],
            ["Rugosa", 3],
            ["Medianamente Rugosa", 0.9],
            ["Rugosa", 3],
            ["Rugosa", 3],
            ["Rugosa", 3],
            ["Rugosa", 3]
        ]

        for i, row in enumerate(table2_roughness):
            for j, value in enumerate(row):
                label = Label(middle_frame, text=value, borderwidth=1, relief="solid", width=16, height=1)
                label.grid(row=i+2, column=j+1, padx=2, pady=2)
    
        roughness_lbl = Label(middle_frame, text='Factor de Rugosidad (mm)', font=('Arial', 15), bg='gray12', fg='gray80')
        roughness_lbl.grid(row=1, column=2, padx=5, pady=3, sticky="nsew")


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
            pressure = f"{app_state.pressure.get():.2f}" if hasattr(app_state.pressure, "get") else app_state.pressure
            temperature = f"{app_state.get_temp.get():.2f}" if hasattr(app_state.get_temp, "get") else app_state.get_temp
            velocity = f"{app_state.velocity_entries[i]:.2f}" if i < len(app_state.velocity_entries) else ''
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

    main_branch_lbl = Label(top_frame, text='El ducto principal se muestra en color rojo en la tabla', font=('Arial', 20), bg='gray12', fg='gray80')
    main_branch_lbl.pack(side='top', pady=1)

    middle_frame = Frame(W, bg='gray12',highlightbackground="red", highlightthickness=2)
    middle_frame.pack(expand=True)
    
    # Get values from the entry fields
    selected =  app_state.selected_option.get()
    rows_number = app_state.duct_number.get()

    # Set the number of rows and columns for the results table
    rows, cols = rows_number, 6

    T = float(app_state.get_temp)

    # Calculate viscosity based on temperature
    if selected == 1 or selected == 2:

        T_K = T + 273.15  # Convert to Kelvin
        mu_0 = 1.716e-5  # Reference viscosity in Pa·s
        T_0 = 273.15  # Reference temperature in K
        Su = 111  # Sutherland's constant in K

        mu = mu_0 * (T_K / T_0) ** 1.5 * (T_0 + Su) / (T_K + Su)  # Sutherland's formula for air viscosity
        viscosity = mu  # Store the viscosity value in app_state
        app_state.viscosity = viscosity

    else:

        # Convert °F to K
        T_K= (T - 32) * 5/9 + 273.1
        T_K= round(T_K, 2)

        # Sutherland's constants (SI base units)
        mu0_si = 1.716e-5     # Pa·s
        T0 = 273.15           # K
        Su = 111.0            # Sutherland's constant for air, K

        # Sutherland’s formula (viscosity in Pa·s)
        mu_si = mu0_si * ((T_K / T0) ** 1.5) * (T0 + Su) / (T_K + Su)

        # Convert Pa·s to lb·s/ft²
        mu_imperial = mu_si * 0.02088543423  # Conversion factor
        viscosity = mu_imperial  # Store the viscosity value in app_state
        app_state.viscosity = viscosity


    # Calculate pressure based on altitude
    H = float(app_state.get_alt) # Convert altitude to float

    # Constants
    P0 = 101325  # Pa
    factor = 0.0000225577
    exponent = 5.2559

    # Calculate pressure in Pascals
    pressure_pa = P0 * (1 - factor * H) ** exponent

    # Convert to appropriate units based on selection
    if selected == 1 or selected == 2:
        pressure = round(pressure_pa, 2)  # Pa
    elif selected == 3:
        pressure = round(pressure_pa * 0.0001450377, 2)  # psi
    else:
        pressure = None

    # Store the result
    app_state.pressure = pressure
    
    
    #calculate density based on temperature and pressure
    
    if selected == 1 or selected == 2:
        T_K = T + 273.15  # °C → K
        R = 287.05  # J/(kg·K) for dry air
        density = pressure / (R * T_K)  # kg/m³

    elif selected == 3:
        T_R = T + 459.67  # °F → °R
        pressure_lbft2 = pressure * 144  # psi → lb/ft²
        R = 53.35  # ft·lb/(lb·°R) for dry air
        density = pressure_lbft2 / (R * T_R)  # lb/ft³
        
    #store the density value in app_state
    app_state.density = density

    #variables to get the values of the flowrate and length
    flowrate_values = app_state.flowrate_entries
    length_values = app_state.length_entries


    # lists to store the results of diameter and friction loss per length
    diameter_values = []
    friction_loss_per_length_values = []
    
    
    for i in range(len(flowrate_values)): # Loop through each branch to calculate diameter and friction loss
        flow_value = flowrate_values[i]
        length_value = length_values[i]

        if selected == 1:
            velocity =  float(app_state.velocity_entries[i])# m/s
            Q = flow_value / 1000  # L/s → m³/s
            diameter_m = math.sqrt((4 * Q) / (math.pi * velocity)) # m
            diameter = diameter_m * 1000  # m → mm
            
            epsilon = 1.5e-7  # roughness for typical duct materials in m
            
            D = diameter_m
            Re = (density * velocity * D) / viscosity

            # Friction factor (turbulent, Swamee-Jain approximation)
            f = 0.25 / ( math.log10( (epsilon / (3.7 * D)) + (5.74 / Re**0.9) ) )**2  # friction factor for turbulent flow

            S = f * (1 / diameter_m) * (density * velocity ** 2) / 2  # Pa per meter

        elif selected == 2:
            velocity = float(app_state.velocity_entries[i])  # m/s
            Q = flow_value  # m³/s
            diameter_m = math.sqrt((4 * Q) / (math.pi * velocity)) # m
            diameter = diameter_m * 1000  # m → mm
            
            epsilon = 1.5e-7  # roughness for typical duct materials in m
            
            D = diameter_m # already in m
            Re = (density * velocity * D) / viscosity # Reynolds number

            # Friction factor (turbulent, Swamee-Jain approximation)
            f = 0.25 / ( math.log10( (epsilon / (3.7 * D)) + (5.74 / Re**0.9) ) )**2  # friction factor for turbulent flow

            # Friction loss per unit length
            S = f * (1 / D) * (density * velocity ** 2) / 2  # Pa per meter

        elif selected == 3:
            velocity = float(app_state.velocity_entries[i])  # fpm (feet per minute)
            Q_ft3s = flow_value / 60  # CFM → ft³/s
            D_ft = math.sqrt((4 * Q_ft3s) / (math.pi * velocity))  # ft
            diameter_in = D_ft * 12  # ft → in
            diameter = diameter_in

            epsilon_in = 0.0005  # typical roughness in inches
            epsilon_ft = epsilon_in / 12  # convert in → ft
            density_ip = app_state.density  # lb/ft³
            viscosity_ip = app_state.viscosity  # lb/ft·s

            D = D_ft  # already in ft
            V_ft_s = velocity / 60  # convert fpm → ft/s
            Re = (density_ip * V_ft_s * D) / viscosity_ip  # Reynolds number

            # Friction factor (turbulent, Swamee-Jain approximation)
            f_ip = 0.25 / (math.log10((epsilon_ft / (3.7 * D)) + (5.74 / Re**0.9))) ** 2

            # Friction loss per unit length
            S_ip = f_ip * (1 / D) * (density_ip * V_ft_s ** 2) / 2  # lb/ft² per ft
            S = S_ip / 5.202  # convert lb/ft² → in.wg per ft

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
            velocity_value = float(app_state.velocity_entries[i])  # m/s
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
        
        preasure_main = Label(middle_frame, text='Presión (psi)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        preasure_main.grid(row=0, column=4)
        
        velocity_main = Label(middle_frame, text='Velocidad (fpm)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        velocity_main.grid(row=0, column=5)       
        
        friction_loses_main = Label(middle_frame, text='Pérdidas por fricción (inH20/ft)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        friction_loses_main.grid(row=0, column=6)
        
        diameter_main = Label(middle_frame, text='Diámetro (in)', font=('Arial', 15), highlightbackground="red", highlightthickness=2, bg='gray12', fg='gray80')
        diameter_main.grid(row=0, column=7) 
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    try_another_speed = Button (bottom_frame, text='Intentar con otra velocidad', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=velocity_entry_menu) 
    try_another_speed.pack(side='left', padx=10, pady=10)
    
    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'),  command=corrections_menu)
    next_btn.pack(side='right' , padx= 10, pady=10)
    
##################################################################################################################################
def save_velocity_data():
    global velocity_entries

    velocities = []

    for i in range(app_state.duct_number.get()):
        try:
            velocity = float(velocity_entries[i].get())
            velocities.append(velocity)
        except ValueError:
            print(f"Error: Ingrese valores válidos en el Ramal {i+1}")

    app_state.velocity_entries = velocities
    print("Velocidades guardadas:", velocities)
    
def velocity_entry_menu():
    #clear the current window
    """Switches to the velocity entry menu where users can input the flow velocity for each branch."""
    global velocity_entries
    for widget in W.winfo_children():
        widget.destroy()
    
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    velocity_lbl = Label(top_frame, text='Ingrese la velocidad del flujo de aire en el ducto principal y los ramales', font=('Arial', 24), bg='gray12', fg='gray80')
    velocity_lbl.pack(side='top', pady=1)
    
    middle_frame = Frame(W, bg='gray12')
    middle_frame.pack(expand=True)
    
    # Get the selected option and duct number from app_state
    selected = app_state.selected_option.get()
    duct_number = app_state.duct_number.get()
    
    # Entry for velocity
    app_state.velocity_entries = []  # Reset stored values
    
    # Header Labels
    headers = {
        1: ("velocidad (m/s)"),
        2: ("velocidad (m/s)"),
        3: ("velocidad (fpm)")
    }
    
    if selected in headers:
        Label(middle_frame, text=headers[selected][0], font=('Arial', 16,'bold'), bg='grey12', fg='grey80').grid(row=0, column=1, padx=5, pady=5)


    velocity_entries = []

    for i in range(duct_number):
        if app_state.main_branch.get() == i + 1:
            Label(middle_frame, text=f'Ramal {i+1} (Principal):', font=('Arial', 14), bg='grey12', fg='red3').grid(row=i+1, column=0, padx=3, pady=1)
        else:
            Label(middle_frame, text=f'Ramal {i+1}:', font=('Arial', 14), bg='grey12', fg='white').grid(row=i+1, column=0, padx=3, pady=1)

        velocity_entry = Entry(middle_frame, font=('Arial', 12), bg='grey40', width=10)
        velocity_entry.grid(row=i+1, column=1, padx=5, pady=1)
        velocity_entries.append(velocity_entry)

        # Placeholder text
    placeholder = 'Escribe aquí...'
    velocity_entry.insert(0, placeholder)

    # Functions to handle placeholder behavior
    def on_focus_in(event):
        if velocity_entry.get() == placeholder:
            velocity_entry.delete(0, 'end')
            velocity_entry.config(fg='black')

    def on_focus_out(event):
        if velocity_entry.get() == '':
            velocity_entry.insert(0, placeholder)
            velocity_entry.config(fg='gray')

    # Bind focus events
    velocity_entry.bind('<FocusIn>', on_focus_in)
    velocity_entry.bind('<FocusOut>', on_focus_out)

    # Auto-focus for caret visibility
    velocity_entry.focus()
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
    
    note_lbl = Label(bottom_frame, text='El valor ingresado se va a usar para el calculo en todos los ramales', font=('Arial', 16), bg='gray12', fg='gray80')
    note_lbl.pack(side='top', pady=1)
    
    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=velocity_range_menu)
    back_btn.pack(side='left', padx=10, pady=10)    
    
    #Button to sumbit the velocity and go to next menu
    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=lambda: [save_velocity_data(), result1_menu()])
    next_btn.pack(side='right', padx=10, pady=10)

###################################################################################################################################

#function to switch to the velocity range menu
def velocity_range_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
    #altitude and temperature menu interface
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    ASHRAE_vel_rec_lbl = Label(top_frame, text='Cualquier sistema de ductos puede diseñarse con ciertos valores máximos admisibles para la velocidad del flujo de aire utilizando los criterios \n de diseño. A continuación se presentan las velocidades de aire recomendadas según los criterios de diseño establecidos por ASHRAE,  \n con el objetivo de garantizar niveles de ruido aceptables y un funcionamiento eficiente de los sistemas de climatización', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
    ASHRAE_vel_rec_lbl.pack(side='top', pady=1)
    
    middle_frame = Frame(W, bg='gray12',highlightbackground="red", highlightthickness=2)
    middle_frame.pack(expand=True)
    
    selected = app_state.selected_option.get()
    if selected == 3:
    #  VELOCITY RANGE MENU FOR IMPERIAL UNITS
    # table 1 velocities for the main duct
    # Create a table to display the recommended air velocities
        
        table1_main_duct_fpm = [
            [45, 3503.94, 5000.0],   # In shaft or above drywall ceiling
            [35, 2500.0, 3503.94],
            [25, 1692.91, 2500.0],
            [45, 2500.0, 4507.87],   # Above suspended acoustic ceiling
            [35, 1751.97, 2992.13],
            [25, 1200.79, 2007.87],
            [45, 2007.87, 3897.64],  # Duct located within occupied space
            [35, 1456.69, 2598.43],
            [25, 944.88, 1692.91]
        ]

        for i, row in enumerate(table1_main_duct_fpm):
            for j, value in enumerate(row):
                label =Label(middle_frame, text=value, borderwidth=1, relief="solid", width=10, height=1)
                label.grid(row=i+3, column=j+1, padx=2, pady=2)

        #table 1 titles
        max_V_main = Label(middle_frame, text='Velocidades máximas del flujo de aire del conducto principal para alcanzar los criterios de diseño acústico', font=('Arial', 20, 'bold'),  borderwidth=2, relief="solid",bg='gray12', fg='gray80')
        max_V_main.grid(row=0, column=0, columnspan=4, padx=5, pady=3, sticky="nsew")

        max_vel_lbl = Label(middle_frame, text='Velocidad máxima del flujo de aire (fpm)', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        max_vel_lbl.grid(row=1, column=2, columnspan=4, padx=3, pady=5, sticky="nsew")

        main_duct_lbl = Label(middle_frame, text='Ubicación del ducto principal', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        main_duct_lbl.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        design_RC_lbl = Label(middle_frame, text='Criterio de diseño', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        design_RC_lbl.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        rect_duct_lbl = Label(middle_frame, text='Ducto rectangular', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        rect_duct_lbl.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        circ_duct_lbl = Label(middle_frame, text='Ducto circular', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        circ_duct_lbl.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        drywall_duct_lbl = Label(middle_frame, text='En espacio vacío o sobre techo de placas de yeso', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        drywall_duct_lbl.grid(row=3, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        suspended_duct_lbl = Label(middle_frame, text='Sobre techo acústico suspendido', font=('Arial', 16), bg='gray12', borderwidth=2, relief="solid", fg='gray80')
        suspended_duct_lbl.grid(row=6, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        occupied_space_duct_lbl = Label(middle_frame, text='Conducto situado dentro de un espacio ocupado', font=('Arial', 16), bg='gray12', borderwidth=2, relief="solid", fg='gray80')
        occupied_space_duct_lbl.grid(row=9, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")
        
        table2_branch_duct_fpm = [
            [45, 2795.28, 3996.06],   # In shaft or above drywall ceiling
            [35, 2007.87, 2795.28],
            [25, 1358.27, 2007.87],
            [45, 2007.87, 3602.36],   # Above suspended acoustic ceiling
            [35, 1397.64, 2401.57],
            [25, 964.57, 1614.17],
            [45, 1614.17, 3110.24],   # Duct located within occupied space
            [35, 1161.42, 2086.61],
            [25, 748.03, 1358.27]
        ]

        for i, row in enumerate(table2_branch_duct_fpm):
            for j, value in enumerate(row):
                label = Label(middle_frame, text=value, borderwidth=1, relief="solid", width=10, height=1)
                label.grid(row=i+15, column=j+1, padx=2, pady=2)

        # table 2 titles
        max_V_branch = Label(middle_frame, text='Velocidad máxima del flujo de aire en los ramales para alcanzar los criterios de diseño acústico', font=('Arial', 20, 'bold'), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        max_V_branch.grid(row=12, column=0, columnspan=4, padx=3, pady=5, sticky="nsew")
        
        max_vel_branch_lbl = Label(middle_frame, text='Velocidad máxima del flujo de aire (m/s)', font=('Arial', 17,'bold'), bg='gray12', fg='gray80')
        max_vel_branch_lbl.grid(row=13, column=2, columnspan=4, padx=3, pady=5, sticky="nsew")
        
        branch_duct_lbl = Label(middle_frame, text='Ubicación del ramal', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        branch_duct_lbl.grid(row=14, column=0, padx=5, pady=5, sticky="nsew")
        
        branch_design_RC_lbl = Label(middle_frame, text='Criterio de diseño', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        branch_design_RC_lbl.grid(row=14, column=1, padx=5, pady=5, sticky="nsew")
        
        branch_rect_duct_lbl = Label(middle_frame, text='Ducto rectangular', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        branch_rect_duct_lbl.grid(row=14, column=2, padx=5, pady=5, sticky="nsew")
        
        branch_circ_duct_lbl = Label(middle_frame, text='Ducto circular', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        branch_circ_duct_lbl.grid(row=14, column=3, padx=5, pady=5, sticky="nsew")

        branch_drywall_duct_lbl = Label(middle_frame, text='En espacio vacío o sobre techo de placas de yeso', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        branch_drywall_duct_lbl.grid(row=15, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        branch_suspended_duct_lbl = Label(middle_frame, text='Sobre techo acústico suspendido', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        branch_suspended_duct_lbl.grid(row=18, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        branch_occupied_space_duct_lbl = Label(middle_frame, text='Conducto situado dentro de un espacio ocupado', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        branch_occupied_space_duct_lbl.grid(row=21, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        note_lbl = Label(middle_frame, text='Los ductos secundarios deben tener velocidades de flujo de aire de aproximadamente del 80% de los valores indicados para el ducto principal.', font=('Arial', 14), bg='gray12', fg='red3')
        note_lbl.grid(row=24, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
    # VELOCITY RANGE MENU FOR METRIC UNITS
    else:
        table1_main_duct = [
            [45, 17.8, 25.4],  # In shaft or above drywall ceiling
            [35, 12.7, 17.8],
            [25, 8.6, 12.7],
            [45, 12.7, 22.9],  # Above suspended acoustic ceiling
            [35, 8.9, 15.2],
            [25, 6.1, 10.2],
            [45, 10.2, 19.8],  # Duct located within occupied space
            [35, 7.4, 13.2],
            [25, 4.8, 8.6]
        ]

        for i, row in enumerate(table1_main_duct):
            for j, value in enumerate(row):
                label =Label(middle_frame, text=value, borderwidth=1, relief="solid", width=10, height=1)
                label.grid(row=i+3, column=j+1, padx=2, pady=2)

        #table 1 titles
        max_V_main = Label(middle_frame, text='Velocidades máximas del flujo de aire del conducto principal para alcanzar los criterios de diseño acústico', font=('Arial', 20, 'bold'),  borderwidth=2, relief="solid",bg='gray12', fg='gray80')
        max_V_main.grid(row=0, column=0, columnspan=4, padx=5, pady=3, sticky="nsew")

        max_vel_lbl = Label(middle_frame, text='Velocidad máxima del flujo de aire (m/s)', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        max_vel_lbl.grid(row=1, column=2, columnspan=4, padx=3, pady=5, sticky="nsew")

        main_duct_lbl = Label(middle_frame, text='Ubicación del ducto principal', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        main_duct_lbl.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

        design_RC_lbl = Label(middle_frame, text='Criterio de diseño', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        design_RC_lbl.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        rect_duct_lbl = Label(middle_frame, text='Ducto rectangular', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        rect_duct_lbl.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")

        circ_duct_lbl = Label(middle_frame, text='Ducto circular', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        circ_duct_lbl.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

        drywall_duct_lbl = Label(middle_frame, text='En espacio vacío o sobre techo de placas de yeso', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        drywall_duct_lbl.grid(row=3, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        suspended_duct_lbl = Label(middle_frame, text='Sobre techo acústico suspendido', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        suspended_duct_lbl.grid(row=6, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        occupied_space_duct_lbl = Label(middle_frame, text='Conducto situado dentro de un espacio ocupado', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        occupied_space_duct_lbl.grid(row=9, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")
        
        # Table 2: Branch duct airflow velocities [RC(N), Rectangular, Circular]
        table2_branch_duct = [
            [45, 14.2, 20.3],  # In shaft or above drywall ceiling
            [35, 10.2, 14.2],
            [25, 6.9, 10.2],
            [45, 10.2, 18.3],  # Above suspended acoustic ceiling
            [35, 7.1, 12.2],
            [25, 4.9, 8.2],
            [45, 8.2, 15.8],   # Duct located within occupied space
            [35, 5.9, 10.6],
            [25, 3.8, 6.9]
        ]

        for i, row in enumerate(table2_branch_duct):
            for j, value in enumerate(row):
                label = Label(middle_frame, text=value, borderwidth=1, relief="solid", width=10, height=1)
                label.grid(row=i+15, column=j+1, padx=2, pady=2)

        # table 2 titles
        max_V_branch = Label(middle_frame, text='Velocidad máxima del flujo de aire en los ramales para alcanzar los criterios de diseño acústico', font=('Arial', 20, 'bold'), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        max_V_branch.grid(row=12, column=0, columnspan=4, padx=3, pady=5, sticky="nsew")
        
        max_vel_branch_lbl = Label(middle_frame, text='Velocidad máxima del flujo de aire (m/s)', font=('Arial', 17,'bold'), bg='gray12', fg='gray80')
        max_vel_branch_lbl.grid(row=13, column=2, columnspan=4, padx=3, pady=5, sticky="nsew")
        
        branch_duct_lbl = Label(middle_frame, text='Ubicación del ramal', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        branch_duct_lbl.grid(row=14, column=0, padx=5, pady=5, sticky="nsew")
        
        branch_design_RC_lbl = Label(middle_frame, text='Criterio de diseño', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        branch_design_RC_lbl.grid(row=14, column=1, padx=5, pady=5, sticky="nsew")
        
        branch_rect_duct_lbl = Label(middle_frame, text='Ducto rectangular', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        branch_rect_duct_lbl.grid(row=14, column=2, padx=5, pady=5, sticky="nsew")
        
        branch_circ_duct_lbl = Label(middle_frame, text='Ducto circular', font=('Arial', 17, 'bold'), bg='gray12', fg='gray80')
        branch_circ_duct_lbl.grid(row=14, column=3, padx=5, pady=5, sticky="nsew")
        
        branch_drywall_duct_lbl = Label(middle_frame, text='En espacio vacío o sobre techo de placas de yeso', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        branch_drywall_duct_lbl.grid(row=15, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        branch_suspended_duct_lbl = Label(middle_frame, text='Sobre techo acústico suspendido', font=('Arial', 16),borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        branch_suspended_duct_lbl.grid(row=18, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        branch_occupied_space_duct_lbl = Label(middle_frame, text='Conducto situado dentro de un espacio ocupado', font=('Arial', 16), borderwidth=2, relief="solid", bg='gray12', fg='gray80')
        branch_occupied_space_duct_lbl.grid(row=21, column=0, rowspan=3, padx=5, pady=5, sticky="nsew")

        note_lbl = Label(middle_frame, text='Los ductos secundarios deben tener velocidades de flujo de aire de aproximadamente del 80% de los valores indicados para el ducto principal.', font=('Arial', 14), bg='gray12', fg='red3')
        note_lbl.grid(row=24, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=branches_features)
    back_btn.pack (side='left', padx=10, pady=10)

    next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=velocity_entry_menu)
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
    global flowrate_entries, length_entries
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
        Button(middle_frame, text='1. L/s    :   Pa/m   : mm : m/s : m ', bg='White', fg='black',
                relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4',
                font=('Arial', 20, 'bold'), command=lambda: select_option(1)),

        Button(middle_frame, text='2. m³/s :   Pa/m   : mm : m/s : m ', bg='White', fg='black',
                relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4',
                font=('Arial', 20, 'bold'), command=lambda: select_option(2)),

        Button(middle_frame, text='3. cfm    : inH20/ft : in : fpm : ft', bg='White', fg='black',
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

    main_branch_lbl = Label(middle_frame, text='Introduzca el número de ramal que va a usar \n como ducto principal:', font=('Arial', 26), bg='gray12', fg='gray80')
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
        print(f'El ducto principal es el número: {app_state.main_branch.get()}')  # Verify it's working
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
