from tkinter import Tk, Label, Button, Entry

# Function to switch to a new menu
def Iniciar():
    # Clear the current window
    for widget in W.winfo_children():
        widget.destroy()
    
    # New Menu Interface
    new_lbl = Label(W, text='El programa va a crear un archivo con los resultados,', font=('Arial', 18, 'bold'), bg='dark slate gray', fg='white')
    new_lbl.pack(pady=1)

    # Entry for file name
    file_name_lbl = Label(W, text='introduzca el nombre con el que quiere guardar el archivo:', font=('Arial', 18, 'bold'), bg='dark slate gray', fg='white')
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

    save_btn = Button(W, text='Guardar archivo', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='DarkSlateGray', font=('Arial', 20, 'bold'), command=save_file_name)
    save_btn.pack(pady=10)

    back_btn = Button(W, text='Volver', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='DarkSlateGray', font=('Arial', 20, 'bold'), command=main_menu)
    back_btn.pack(side='bottom', pady=50)

# Function to return to the main menu
def main_menu():
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()

    # Original Main Menu
    lbl1 = Label(W, text='DIMENSIONAMIENTO DE DUCTOS', font=('Arial', 20, 'bold'), bg='DarkSlateGray')
    lbl1.pack(pady=1)

    lbl2 = Label(W, text='DE AIRE ACONDICIONADO', font=('Arial', 20, 'bold'), bg='DarkSlateGray')
    lbl2.pack(pady=1)

    btn1 = Button(W, text='Iniciar', bg='DarkSlateGray', fg='black', relief='raised', activebackground='SlateGray', activeforeground='white', highlightbackground='DarkSlateGray', font=('Arial', 20, 'bold'), command=Iniciar)
    btn1.pack(pady=1)

    lbl4 = Label(W, text='Desarrollado por Luis Jimenez', font=('Arial', 8, 'bold'), bg='DarkSlateGray')
    lbl4.pack(side='bottom', pady=1)

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
W.config(bg='DarkSlateGray')

# Load the main menu initially
main_menu()

W.mainloop()
