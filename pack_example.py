from tkinter import Tk, Label, Button, Entry

W = Tk()
W.title('pack example')
W.geometry('400x230')
W.config(bg='slate gray')

def fnsuma():
    n1 = txt1.get()
    n2 = txt2.get()
    r  = float(n1) + float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,r) 

lbl1 = Label (W,text='first number', bg='coral1')
lbl1.pack(pady=5)
txt1 = Entry(W, bg= 'SkyBlue1')
txt1.pack(pady=5)

lbl2 = Label(W,text='second number', bg='coral1')
lbl2.pack(pady=5) 
txt2 = Entry(W, bg= 'SkyBlue1')
txt2.pack(pady=5)

lbl3 = Label(W,text='result', bg='coral1')
lbl3.pack(pady=5) 
txt3 = Entry(W, bg= 'SkyBlue1')
txt3.pack(pady=5)
 
btn1 = Button(W, bg='lemon chiffon', text='sum', command=fnsuma)
btn1.pack(pady=5)


W.mainloop()