import tkinter as tk

class Model:
    def __init__(self):
        self.n1 = tk.IntVar(0)

    def get_numero(self):
        return self.n1

    def set_numero(self,n1):
        self.n1 = n1

class View (tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.lbln1=tk.Label(self.parent, text="Numero 1")
        self.lbln1.grid( row=0,column=0)
        self.txtn1=tk.Entry()
        self.txtn1.grid(row=0,column=1)

        self.btnguardar=tk.Button(text="Guardar")
        self.btnguardar.grid(row=2,column=0)

        self.btnmostrar=tk.Button(text="Mostrar")
        self.btnmostrar.grid(row=2,column=1)

        self.lblres=tk.Label(self.parent, text="Resultado")
        self.lblres.grid(row=3,column=0)

        self.parent.geometry("500x300")

    def mostrar_resultado(self, message):
        self.lblres['text'] = message        

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root)

        self.view.btnguardar.config(command=self.guardar_numero)
        self.view.btnmostrar.config(command=self.muestra_numero)

    def guardar_numero(self):
        self.model.set_numero(self.view.txtn1.get())    

    def muestra_numero(self):
        try:
            n1 = self.model.get_numero()
            self.view.lblres['text'] = n1
        except Exception as e:
            print(e)

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()

"""  
import tkinter as tk

class Vista:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Programa ")
        self.ventana1.geometry("500x300")
        self.lbln1=tk.Label(self.ventana1, text="Numero 1")
        self.lbln1.grid( row=0,column=0)
        self.txtn1=tk.Entry()
        self.txtn1.grid(row=0,column=1)

        self.lbln2=tk.Label(self.ventana1, text="Numero 2")
        self.lbln2.grid(row=1,column=0)
        self.txtn2=tk.Entry()
        self.txtn2.grid(row=1,column=1)   

        self.lblres=tk.Label(self.ventana1, text="Resultado")
        self.lblres.grid(row=3,column=0)
        self.btncalcular=tk.Button(text="Calcular",command= self.boton_guardar_clicked)
        self.btncalcular.grid(row=2,column=0)

        self.control = None
        self.ventana1.mainloop()

    def mostrar_resultado(self, message):
        self.lblres['text'] = message

    def set_control(self, control):
        self.control = control

    def boton_guardar_clicked(self):
        if self.control:
            self.control.mostrar_resultado(self.lbln1.get())
 

class Modelo:
    def __init__(self,n1):
        self.numero1 = n1

    def set_numero1(self,n1):
        self.numero1 = n1        

    def get_numero1(self):
        return self.numero1       

class Controlador:

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def muestra_numero (self, n1):
        self.modelo.numero1 = n1
        self.vista.mostrar_resultado(f'El numero es {n1}')

class App:
    def __init__(self):
        super().__init__()
        modelo = Modelo(2)
        vista = Vista()
        control = Controlador(modelo,vista)
        vista.set_control(control)       

if __name__ == '__main__':
    ap = App()
"""  