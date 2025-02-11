from tkinter import Tk, Label, Entry, Button

try:
    for widget in Tk._default_root.winfo_children():
        widget.destroy()
    Tk._default_root.destroy()
except AttributeError:
    pass

W = Tk()
W.title('place example')
W.geometry('500x400')
W.config(bg='DarkSlateGray')
 
lbl1 = Label (W,text='DIMENSIONAMIENTO DE DUCTOS', font=('Arial', 20, 'bold'), bg='DarkSlateGray')
lbl1.pack(pady=1)

lbl2 = Label (W,text='DE AIRE ACONDICIONADO', font=('Arial', 20, 'bold'), bg='DarkSlateGray')
lbl2.pack(pady=1)

lbl3 = Label (W,text='Desarrollado por Luis Jimenez', font=('Arial', 6, 'bold'), bg='coral1')
lbl3.place(x=230, y=380, width=100, height=30)

W.mainloop()

