from tkinter import Button, Label, Entry

def file_name_menu(W):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()

    Label(W, text="Ingrese el nombre del archivo:",
         font=('Arial', 20), bg='gray12', fg='gray80').pack(pady=10)

    Entry(W, font=('Arial', 18)).pack(pady=10)

    # ✅ Local import avoids circular import
    from menus.main_menu import main_menu  
    Button(W, text="Volver",
           bg='DarkSlateGray', fg='black',
           relief='raised',
           activebackground='SlateGray',
           activeforeground='white',
           highlightbackground='brown4',
           font=('Arial', 18, 'bold'),
           command=lambda: main_menu(W)).pack(pady=20)