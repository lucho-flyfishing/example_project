from tkinter import Tk, Label, Entry, Button

W = Tk()
W.title('grid example')
W.geometry('400x230')
W.config(bg='slate gray')

def fnsuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r  = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,r) 

lbl1 = Label (W,text='first number', bg='coral1')
lbl1.grid(row=0, column=0, padx=5, pady=5)
txt1 = Entry(W, bg= 'SkyBlue1')
txt1.grid(row=0, column=1, padx=5, pady=5)

lbl2 = Label(W,text='second number', bg='coral1')
lbl2.grid(row=1, column=0, padx=5, pady=5) 
txt2 = Entry(W, bg= 'SkyBlue1')
txt2.grid(row=1, column=1, padx=5, pady=5)

lbl3 = Label(W,text='result', bg='coral1')
lbl3.grid(row=2, column=0, padx=5, pady=5) 
txt3 = Entry(W, bg= 'SkyBlue1')
txt3.grid(row=2, column=1, padx=5, pady=5)
 
btn1 = Button(W, bg='lemon chiffon', text='sum', command=fnsuma)
btn1.grid(row=1, column=2,padx=5, pady=5) 


W.mainloop()