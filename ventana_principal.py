import tkinter as tk
from Controladores.ventana_principal_Controlador import *
from Controladores.ventana_dos_Controlador import *
from Controladores.ventana_tres_Controlador import *
from tkinter import *

class Aplicacion:
    def __init__(self):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Menu principal")
        self.configurar_ventana()
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

    def configurar_ventana(self):
        wventana = 1080
        hventana = 600

        wtotal = self.ventana_principal.winfo_screenwidth()
        htotal = self.ventana_principal.winfo_screenheight()
        pwidth = round(wtotal/2-wventana/2)
        pheight = round(htotal/2-hventana/2)

        self.ventana_principal.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))
        self.ventana_principal.resizable(0, 0)