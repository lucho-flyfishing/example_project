from tkinter import Button, Label

def main_menu(W):
    # Clear the window
    for widget in W.winfo_children():
        widget.destroy()

    # Original Main Menu
    lbl1 = Label(W, text='DIMENSIONAMIENTO DE DUCTOS \n DE AIRE ACONDICIONADO',
                 font=('Arial', 30, 'bold'), bg='gray12', fg='brown2')
    lbl1.pack(pady=1)

    lbl2 = Label(W, text='Con este programa usted podrá dimensionar ductos de ventilación \n'
                         'considerando las pérdidas debidas a la fricción en tramos rectos y \n'
                         'en accesorios. Solo es necesario conocer el caudal en los \n'
                         'ramales del sistema. Además, el programa presenta los ductos \n'
                         'rectangulares equivalentes.',
                 font=('Arial', 26), bg='gray12', fg='gray80')
    lbl2.pack(pady=1)

    lbl3 = Label(W, text='(En los cálculos se incluyen las correcciones debidas a la altitud, \n'
                         'la temperatura y la rugosidad.)',
                 font=('Arial', 16), bg='gray12', fg='gray80')
    lbl3.pack(pady=1)

    # ✅ Local import avoids circular import
    from menus.file_name_menu import file_name_menu  
    start_button = Button(W, text='Iniciar',
                          bg='DarkSlateGray', fg='black',
                          relief='raised',
                          activebackground='SlateGray',
                          activeforeground='white',
                          highlightbackground='brown4',
                          font=('Arial', 24, 'bold'),
                          command=lambda: file_name_menu(W))
    start_button.pack(pady=30)

    lbl5 = Label(W, text='Desarrollado en la Universidad del Valle por Luis Jimenez',
                 font=('Arial', 12, 'bold'), bg='gray12', fg='gray80')
    lbl5.pack(side='bottom', pady=1)