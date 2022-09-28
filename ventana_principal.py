import tkinter as tk
from ventana_principal_Controlador import *
from ventana_dos_Controlador import *
from ventana_tres_Controlador import *
from tkinter import *

class Aplicacion:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Menu principal")
        self.ventana_principal.geometry("600x400")
        self.lblnombrev2=tk.Label(self.ventana_principal,text="Ventana")
        self.lblnombrev2.grid(row=0,column=0)
        self.menuppal = tk.Menu(self.ventana_principal)
        self.opciones = tk.Menu(self.menuppal)
        self.opciones.add_command(label="Ventana 1", command = self.ventana_uno)
        self.opciones.add_command(label="Ventana 2", command = self.ventana_dos)
        self.opciones.add_command(label="Ventana 3", command = self.ventana_tres)
        self.menuppal.add_cascade(label="Opciones", menu=self.opciones)
        self.ventana_principal.config(menu=self.menuppal)
        self.ventana_principal.mainloop()

    def ventana_uno(self):
        root = tk.Tk()
        control = Ventana_Principal_Controller(root)
        root.mainloop()
    def ventana_dos(self):
        root2 = tk.Tk()
        control_ventana_dos = Ventana_Dos_Controller(root2)
        root2.mainloop()
    def ventana_tres(self):
        root3 = tk.Tk()
        control_ventana_tres = Ventana_Tres_Controller(root3)
        root3.mainloop()
