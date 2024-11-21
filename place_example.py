from tkinter import Tk, Label, Entry, Button 

W = Tk()
W.title('place example')
W.geometry('450x200')
W.config(bg='NavajoWhite3')

def fnsuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r  = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,r) 

lbl1 = Label (W,text='first number', bg='coral1')
lbl1.place(x=10, y=10, width=100, height=30)
txt1 = Entry(W, bg= 'brown2')
txt1.place(x=120, y=10, width=150, height=30)

lbl2 = Label(W,text='second number', bg='coral1')
lbl2.place(x=10, y=50, width=100, height=30) 
txt2 = Entry(W, bg= 'brown2')
txt2.place(x=120, y=50, width=150, height=30)

lbl3 = Label(W,text='result', bg='coral1')
lbl3.place(x=10, y=120, width=100, height=30) 
txt3 = Entry(W, bg= 'brown2')
txt3.place(x=120, y=120, width=150, height=30)
 
btn1 = Button(W, bg='lemon chiffon', text='sum', command=fnsuma)
btn1.place(x=290, y=50, width=150, height=30)
W.mainloop()
