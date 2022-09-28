import tkinter as tk
from ventana_principal_Controlador import *

class Aplicacion:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Menu principal")
        self.ventana_principal.geometry("600x400")
        self.lblnombrev2=tk.Label(self.ventana_principal,text="Ventana")
        self.lblnombrev2.grid(row=0,column=0)
        self.menuppal =tk.Menu(self.ventana_principal)
        self.ventana_principal.config(menu=self.menuppal)
        self.opciones = tk.Menu(self.menuppal)
        self.opciones.add_command(label="Modulo 1", command = self.ventana_uno)
        self.menuppal.add_cascade(label="Opciones", menu=self.opciones)
        self.ventana_principal.mainloop()

    def ventana_uno(self):
        root = tk.Tk()
        control = Controller(root)
        root.mainloop()
    def ventana_dos(self):
        pass
    def ventana_tres(self):
        pass
