from tkinter import Tk, Label, Entry, Button

try:
    for widget in Tk._default_root.winfo_children():
        widget.destroy()
    tk._default_root.destroy()
except AttributeError:
    pass

W = Tk()
W.title('place example')
W.geometry('500x400')
W.config(bg='DarkSlateGray')

lbl1 = Label (W,text='DIMENSIONAMIENTO DE DUCTOS', font=('Arial', 20, 'bold'), bg='DarkSlateGray')
lbl1.place(x=75, y=10, width=350, height=30)
lbl1 = Label (W,text='DE AIRE ACONDICIONADO', font=('Arial', 20, 'bold'), bg='DarkSlateGray')
lbl1.place(x=85, y=35, width=350, height=20)

lbl1 = Label (W,text='Desarrollado por Luis Jimenez', font=('Arial', 6, 'bold'), bg='DarkSlateGray')
lbl1.place(x=75, y=380, width=350, height=30)


W.mainloop()

