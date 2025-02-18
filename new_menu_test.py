#el orden de los menus es el siguiente: menu3 -> menu2 -> menu1 -> main_menu
#cada menu tiene un boton para volver al menu anterior y otro para ir al siguiente menu
#el menu 1 tiene un boton para guardar el nombre del archivo que se va a crear


from tkinter import Tk, Label, Button, Entry, Frame


#function to switch duct features
    
branch_data = {}

def save_branch_data():
    """Save the flow rate and length for each branch."""
    for i in range(duct_number):
        branch_data[f'branch{i+1}_flowrate'] = flowrate_entries[i].get()
        branch_data[f'branch{i+1}_length'] = length_entries[i].get()

    print(branch_data)  # Debugging: Print saved values

def branches_features():
    """Create a menu with input fields for flow rate and length of each branch."""
    global middle_frame, flowrate_entries, length_entries
    for widget in W.winfo_children():
        widget.destroy()

    Label(W, text="Ingrese los valores de cada ramal", font=('Arial', 16, 'bold'), bg='grey12', fg='grey80').pack(pady=10)

    # Frame to hold entry fields
    middle_frame = Frame(W, bg='grey12')
    middle_frame.pack(pady=10)

    flowrate_entries = []
    length_entries = []

    # Header Labels
    Label(middle_frame, text="Caudal (m³/h)", font=('Arial', 12), bg='grey12', fg='grey80').grid(row=0, column=1, padx=5, pady=5)
    Label(middle_frame, text="Longitud (m)", font=('Arial', 12), bg='grey12', fg='grey80').grid(row=0, column=2, padx=5, pady=5)

    # Create input fields for each branch
    for i in range(duct_number):
        Label(middle_frame, text=f'Ramal {i+1}:', font=('Arial', 12), bg='DarkSlateGray', fg='white').grid(row=i+1, column=0, padx=5, pady=5)
        
        flowrate_entry = Entry(middle_frame, font=('Arial', 12), width=10)
        flowrate_entry.grid(row=i+1, column=1, padx=5, pady=5)
        flowrate_entries.append(flowrate_entry)

        length_entry = Entry(middle_frame, font=('Arial', 12), width=10)
        length_entry.grid(row=i+1, column=2, padx=5, pady=5)
        length_entries.append(length_entry)

    # Save Button
    save_btn = Button(W, text="Guardar y Continuar", bg="DarkSlateGray", fg="black", font=('Arial', 14, 'bold'),command=save_branch_data)
    save_btn.pack(pady=10)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn_m2 = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=menu3)
    back_btn_m2.pack (side='left', padx=10, pady=10)

    next_btn_m2 = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'))
    next_btn_m2.pack(side='right' , padx= 10, pady=10)

#function to switch to the menu 3
def menu3():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
        
    #menu 3 interface
    top_frame = Frame(W, bg='gray12')
    top_frame.pack(side='top', fill='x')
    
    menu3_lbl = Label(top_frame, text='El programa permite escoger entre tres sistemas \n de unidades, selecione las unidades para: caudal, \n perdidas, diametro y  velocidad respectivamente', font=('Arial', 24, 'bold'), bg='gray12', fg='gray80')
    menu3_lbl.pack(side='top', pady=1)
    
    #selecion de unidades
    middle_frame = Frame(W, bg='gray12')
    middle_frame.pack(expand=True)
    
    unidades_lbl = Label(middle_frame, text='UNIDADES', font=('Arial', 25, 'bold'), bg='gray12', fg='gray80')
    unidades_lbl.grid(row=0, column=2)
    
    menu3_opt_1 = Button (middle_frame, text='1. L/s    :   Pa/m   : mm : m/s : m ', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'))
    menu3_opt_1.grid(row=1, column=2, padx=5, pady=5)
    
    menu3_opt_2 = Button (middle_frame, text='2. m^3/s :   Pa/m   : mm : m/S : m ', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'))
    menu3_opt_2.grid(row=2, column=2, padx=5, pady=5)
    
    menu3_opt_3 = Button (middle_frame, text='3. cfm    : inH20/ft : mm : fpm : ft', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'))
    menu3_opt_3.grid(row=3, column=2, padx=5, pady=5)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn_m2 = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=duct_number_menu)
    back_btn_m2.pack (side='left', padx=10, pady=10)

    next_btn_m2 = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'),  command=branches_features)
    next_btn_m2.pack(side='right' , padx= 10, pady=10)


#function to switch to the menu 2

def duct_number_menu():
    #clear the current window
    for widget in W.winfo_children():
        widget.destroy()
    
    # Entry for duct number
    duct_number_lbl = Label(W, text='Introduzca la cantidad de ramales del ducto, luego \n presione siguiente:', font=('Arial', 24, 'bold'), bg='gray12', fg='gray80')
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

    # Function to save duct number
    def save_duct_number():
        global duct_number
        duct_number = duct_number_entry.get()
    
        if duct_number == duct_number_placeholder:
            duct_number = ''  # Avoid saving placeholder as file name
        else:
            try:
                duct_number = int(duct_number)  # Convert to integer
            except ValueError:
                print("Error: Ingrese un número válido")  # Handle non-numeric input

        print(f'el número de ductos es: {duct_number}')  # Verify it's working
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn_m2 = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='Brown4', font=('Arial', 20, 'bold'), command=menu1)
    back_btn_m2.pack (side='left', padx=10, pady=10)

    next_btn_m2 = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='Brown4', font=('Arial', 20, 'bold'), command=lambda: [save_duct_number(), menu3()])
    next_btn_m2.pack(side='right' , padx= 10, pady=10)


# menu 1 interface
def menu1():
    # Clear the current window
    for widget in W.winfo_children():
        widget.destroy()
    
    # New Menu Interface
    
    # Entry for file name
    file_name_lbl = Label(W, text='El programa va a crear un archivo con los \n resultados, introduzca el nombre con el que \n quiere guardar el archivo, luego presione siguiente:', font=('Arial', 24, 'bold'), bg='gray12', fg='gray80')
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

    # Function to save the file name
    def save_file_name():
        global file_name
        file_name = file_name_entry.get()
        if file_name == placeholder:
            file_name = ''  # Avoid saving placeholder as file name
        print(f'Nombre del archivo guardado: {file_name}')  # Just to verify it's working

    save_btn = Button(W, text='Guardar archivo', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=save_file_name)
    save_btn.pack(pady=10)
    
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')

    back_btn_m1 = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=main_menu)
    back_btn_m1.pack(side='left', padx=10, pady=10)

    next_btn_m1 = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=duct_number_menu)
    next_btn_m1.pack(side='right' , padx= 10, pady=10)

# Function to return to the main menu
# menu principal
def main_menu():
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()

    # Original Main Menu
    lbl1 = Label(W, text='DIMENSIONAMIENTO DE DUCTOS \n DE AIRE ACONDICIONADO', font=('Arial', 25, 'bold'), bg='gray12', fg='brown2')
    lbl1.pack(pady=1)
    
    lbl2 = Label(W, text='Con este programa usted podra dimensionar ductos de ventilacion \n considerando las perdidas debidas a la friccion en tramos rectos y \n en accesorios. Solo es necesario conocer el caudal en los \n rameles del sistema, ademas, el programa presenta los ductos \n rectangulares equivalentes', font=('Arial', 20), bg='gray12', fg='gray80')
    lbl2.pack(pady=1)

    lbl3 = Label(W, text='(En los calculos se incluyen las correciones debidas a la altitud, \n temperatura y rugosidad)', font=('Arial', 10), bg='gray12', fg='gray80')
    lbl3.pack(pady=1)
    
    start_button = Button(W, text='Iniciar', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=menu1)
    start_button.pack(pady=30)

    lbl5 = Label(W, text='Desarrollado en la Universidad del Valle por Luis Jimenez', font=('Arial', 8, 'bold'), bg='gray12', fg='gray80')
    lbl5.pack(side='bottom', pady=1)

# Main Window Setup
try:
    for widget in Tk._default_root.winfo_children():
        widget.destroy()
    Tk._default_root.destroy()
except AttributeError:
    pass

W = Tk()
W.title('Dimensionamiento de Ductos')
W.geometry('600x600')
W.config(bg='gray12')

# Load the main menu initially
main_menu()

W.mainloop()
