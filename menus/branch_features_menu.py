from tkinter import Label, Button, Frame

import app_state

def branch_features_menu(W, go_back):
    for widget in W.winfo_children():
        widget.destroy()
    
    lbl = Label(W, text='Branch Features Menu - To be implemented',
                font=('Arial', 30, 'bold'), bg='gray5', fg='Dark Orange')
    lbl.pack(pady=20)
    
    
    if app_state.app_state.selected_option.get() == 1:
        lbl_selected = Label(W, text='Selected Units: 1. L/s : Pa/m : mm : m/s : m',
                            font=('Arial', 20), bg='gray5', fg='Light Green')
        lbl_selected.pack(pady=10)
    elif app_state.app_state.selected_option.get() == 2:
        lbl_selected = Label(W, text='Selected Units: 2. m³/s : Pa/m : mm : m/s : m',
                            font=('Arial', 20), bg='gray5', fg='Light Green')
        lbl_selected.pack(pady=10)
    elif app_state.app_state.selected_option.get() == 3:
        lbl_selected = Label(W, text='Selected Units: 3. cfm : inH20/ft : in : fpm : ft',
                            font=('Arial', 20), bg='gray5', fg='Light Green')
        lbl_selected.pack(pady=10)
    
        
    bottom_frame = Frame(W, bg='gray12')
    bottom_frame.pack(side='bottom', fill='x')
        
    back_btn = Button(bottom_frame, text='Volver', 
                    bg='White', fg='black',
                    relief='raised', 
                    activebackground='DodgerBlue2', 
                    activeforeground='OrangeRed2', 
                    font=('Arial', 20, 'bold'),
                    command=lambda: go_back(W))
    back_btn.pack(side='left', padx=10, pady=10)

