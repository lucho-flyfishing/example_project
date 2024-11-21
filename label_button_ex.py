from tkinter import Tk, Label, Button

def mensaje ():
    print('has sido exterminado')
    
ventana = Tk() #clase para crear una ventana principal donde añadir widgets
ventana.geometry('600x600')
ventana.config(bg='black')
ventana.title(':)')

lbl = Label(ventana, text='Este es un [Label] Tkinter')
lbl.config(bg='black', fg='red')
lbl.pack() #ubica los widgets en una posicion que podemos cambiar a traves de los correspondientes atributos

btn = Button(ventana, text= 'presiona este [Button] para mensaje', command = mensaje)
btn.config( bg ='black', fg= 'green',) 
btn.pack()


ventana.mainloop() #inicia el bucle de mensajes, aqui se monitorea la interaccion del usario a traves del raton o teclado.

