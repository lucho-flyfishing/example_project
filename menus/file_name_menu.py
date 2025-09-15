from tkinter import Button, Label, Entry

def file_name_menu(W):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()

    Label(W, text="Ingrese el nombre del archivo:",
        font=('Arial', 20), bg='gray5', fg='gray80').pack(pady=10)

    Entry(W, font=('Arial', 18)).pack(pady=10)

    # back button to return to main menu
    from menus.main_menu import main_menu  
    Button(W, text="Volver",
        bg='DodgerBlue4', fg='DodgerBlue1',
        relief='raised',
        activebackground='SlateGray',
        activeforeground='white',
        highlightbackground='brown4',
        font=('Arial', 18, 'bold'),
        command=lambda: main_menu(W)).pack(pady=20)
    
    # function to switch to the file name menu
#def file_name_menu():
    # Clear the current window
    #for widget in W.winfo_children():
        #widget.destroy()
    
    # New Menu Interface
    
    # Entry for file name
    #file_name_lbl = Label(W, text='El programa va a crear un archivo con los \n resultados. Introduzca el nombre con el que \n desea guardar el archivo y presione "Guardar\n nombre del archivo", luego presione “Siguiente”:', font=('Arial', 26), bg='gray12', fg='gray80')
    #file_name_lbl.pack(pady=1)

    #file_name_entry = Entry(W, font=('Arial', 12), bg='white', fg='gray', relief='solid', bd=2, highlightthickness=2, highlightbackground='black')
    #file_name_entry.pack(pady=5, ipady=5, ipadx=10)

    # Placeholder text
    #placeholder = 'Escribe aquí...'
    #file_name_entry.insert(0, placeholder)

    # Functions to handle placeholder behavior
    #def on_focus_in(event):
        #if file_name_entry.get() == placeholder:
            #file_name_entry.delete(0, 'end')
            #file_name_entry.config(fg='black')

    #def on_focus_out(event):
        #if file_name_entry.get() == '':
            #file_name_entry.insert(0, placeholder)
            #file_name_entry.config(fg='gray')

    # Bind focus events
    #file_name_entry.bind('<FocusIn>', on_focus_in)
    #file_name_entry.bind('<FocusOut>', on_focus_out)
    
    # Auto-focus for caret visibility
    #file_name_entry.focus()

    #def save_filename():
        #filename = file_name_entry.get()
    
        #if filename == placeholder or filename.strip() == "":
            #print("Nombre de archivo inválido.")
        #else:
            #app_state.filename.set(filename)  # Save the value
            #print(f"Guardando como: {app_state.filename.get()}")  # Print to verify
        
    #save_btn = Button(W, text='Guardar nombre del archivo', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=save_filename)
    #save_btn.pack(pady=10)
    
    #bottom_frame = Frame(W, bg='gray12')
    #bottom_frame.pack(side='bottom', fill='x')

    #back_btn = Button(bottom_frame, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=main_menu)
    #back_btn.pack(side='left', padx=10, pady=10)

    #next_btn = Button(bottom_frame, text='Siguiente', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='brown4', font=('Arial', 20, 'bold'), command=duct_number_menu)
    #next_btn.pack(side='right' , padx= 10, pady=10)